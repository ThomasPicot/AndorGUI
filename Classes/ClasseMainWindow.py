import pyqtgraph as pg
from Classes.TrigExtThread import Worker
from Classes.ClasseAndor import AndorCam
from Classes.ui_AndorCam import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initiates the Ui_MainWindow() class that I wrote in ui_AndorCam.py file.
        Initiates AndorCam() class that is the interface of the device Andor.
        setup the UI.
        As this file MUST not being touched, you need to connect buttons and methods
        in this class.
        initiates the attributes for the ROIs and the worker thread.
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.andor = AndorCam()
        self.ui.setupUi(self)
        self._number_frame = 0
        self.worker_thread = Worker(self)
        self.roi_norm = None
        self.cam_roi = None
        self.same_exposure_than_before = None
        self.trig_mode = None
        self.acquistion = False
        self.main_view = self.ui.widgetFrame.addViewBox()
        #self.main_view.
        self.resizeEvent = self.on_resize   # used to make the display of widgetFrame always square 
        self.crosshair_h = None
        self.crosshair_v = None
        self.crosshair_enabled = False
        
        # parametrize plot widgets
        self.main_view.scene().sigMouseClicked.connect(self.mouse_click_event)
        self.ui.widget_Vcut.plotItem.hideAxis('bottom')
        self.ui.widget_Vcut.plotItem.hideAxis('left')
        self.ui.widget_Hcut.plotItem.hideAxis('bottom')
        self.ui.widget_Hcut.plotItem.hideAxis('left')
        # __________________________________________________________________________
        # connect buttons with methods
        # __________________________________________________________________________

        # acquisition part _________________________________________________________
        self.ui.pushButton_shot.clicked.connect(self.display_image_int)
        self.ui.pushButton_start_ext.clicked.connect(self.start_thread)
        self.ui.pushButton_stop_ext.clicked.connect(self.stop_thread)
        self.ui.pushButton_normalisation.clicked.connect(
            self.toggle_normalization)
        self.ui.pushButton_setROI.clicked.connect(self.set_ROI)
        self.ui.pushButton_apply_ROI.clicked.connect(self.apply_ROI)
        self.ui.pushButton_clear_ROI.clicked.connect(self.clear_ROI)
        self.ui.pushButton_clear_crosshair.clicked.connect(self.clear_crosshair)
        # saving data part _________________________________________________________
        self.ui.pushButton_start_acq.clicked.connect(self.start_acquisition)
        self.ui.pushButton_stop_acq.clicked.connect(self.stop_acquisition)

    def display_image_int(self):
        """
        method of the class MainWindow that conditionally setup the acquisition with the exposure of the doubleSpinBox,
        take a picture with 'snap' mode
        :return:None
        """
        self.main_view.clear()

        current_exposure_time = float(self.ui.doubleSpinBox_exposure.value())
        current_trig_mode = 'int'

        # Check if trigger mode or exposure time has changed
        if (self.trig_mode != current_trig_mode or
                self.exposure_time != current_exposure_time * 1e-3):
            # Trigger mode or exposure time has changed, setup acquisition
            self.andor.set_acquisition(acquisition_mode=0, exposure_time=current_exposure_time * 1e-3,
                                       trigger_mode=current_trig_mode, frame_method='snap')

            # Update exposure time and trigger mode attributes
            self.exposure_time = current_exposure_time * 1e-3
            self.trig_mode = current_trig_mode

        # Acquire image
        self.image_data = np.array(self.andor.acquisition())

        # Display image
        if self.roi_norm is not None:
            normalized_image_data = self.image_data / self.roi_norm_mean
            self.image_item = pg.ImageItem(image=normalized_image_data)
        else:
            self.image_item = pg.ImageItem(image=self.image_data)
        self.main_view.addItem(self.image_item)
        # if there is a crosshair:
        if self.crosshair_enabled is True:
            self.plot_crosshair()
        
        self._number_frame += 1
        self.ui.textBrowserLogs.clear()
        self.ui.textBrowserLogs.append(
            "Frame number : "+str(self._number_frame))

    def display_image_ext(self):
        """
        method of the class MainWindow that works with GoodTime sequences. Setup the acquisition, take images
        and add the image on the main_view.
        Works in worker_thread.
        :return: None
        """
        current_exposure_time = float(self.ui.doubleSpinBox_exposure.value())
        current_trig_mode = 'ext'

        # Check if trigger mode or exposure time has changed
        if (self.trig_mode != current_trig_mode or
                self.exposure_time != current_exposure_time * 1e-3):
            # Trigger mode or exposure time has changed, set acquisition parameters
            self.andor.set_acquisition(acquisition_mode=0, exposure_time=current_exposure_time * 1e-3,
                                       trigger_mode=current_trig_mode, frame_method='snap')

            # Update exposure time and trigger mode attributes
            self.exposure_time = current_exposure_time * 1e-3
            self.trig_mode = current_trig_mode

        # Acquire image
        self.image_data = np.array(self.andor.acquisition())

        # Display image
        if self.roi_norm is not None:
            self.image_data = self.image_data / self.roi_norm_mean
            self.image_item = pg.ImageItem(image=self.image_data)
        else:
            self.image_item = pg.ImageItem(image=self.image_data)

        self.main_view.addItem(self.image_item)
        self._number_frame += 1
        # self.ui.textBrowserLogs.clear()
        self.ui.textBrowserLogs.append(
            "Frame number : "+str(self._number_frame))
        if self.acquistion is True:
            self.acquisition_data.append(self.image_data)
        if self.crosshair_enabled is True:
            self.plot_crosshair()

    def start_thread(self):
        """
        start thread with the button start
        :return: None
        """
        self.worker_thread = Worker(self)
        self.worker_thread.start()
        self._number_frame = 0
        self.main_view.clear()

    def stop_thread(self):
        """
        stop the thread
        :return: None
        """
        if self.worker_thread is not None and self.worker_thread.isRunning():
            self.worker_thread.requestInterruption()
            self.ui.textBrowserLogs.append("Stopping thread")
            self.worker_thread.wait(1000)
            self.worker_thread.quit()
            self._number_frame = 0

    def toggle_normalization(self):
        """
        method of class MainWindow that applies or not the normalization to the image.
        :return: None
        """
        if self.roi_norm is None:
            # Create ROI the first time the button is clicked
            self.roi_norm = pg.RectROI([1020, 1020], [300, 300], pen=(0, 9))
            self.main_view.addItem(self.roi_norm)
            self.roi_norm.sigRegionChangeFinished.connect(
                self.roi_norm_changed)
        else:
            # Toggle ROI visibility
            self.roi_norm.setVisible(not self.roi_norm.isVisible())
            self.roi_norm = None

    def roi_norm_changed(self):
        """
        method of class MainWindow. If the ROI of the norm changes, update the image.

        :return: None
        """
        self.roi_norm_pos = self.roi_norm.pos()
        self.roi_norm_size = self.roi_norm.size()
        # Extract the region within the ROI
        x, y, w, h = self.roi_norm_pos[0], self.roi_norm_pos[1], self.roi_norm_size[0], self.roi_norm_size[1]
        self.roi_norm_data = self.image_data[int(
            y):int(y + h), int(x):int(x + w)]

        # Calculate the mean of all points within the ROI
        self.roi_norm_mean = np.mean(self.roi_norm_data)

        # Divide the entire image by the mean of the ROI
        normalized_image_data = self.image_data / self.roi_norm_mean
        # Update the image item with the normalized data
        self.image_item = pg.ImageItem(image=normalized_image_data)
        self.main_view.addItem(self.image_item)

    def set_ROI(self):
        """
        method of class MainWindow that set the ROI of the camera.
        :return:
        """
        self.cam_roi = pg.RectROI([1020, 200], [300, 300], pen={
                                  'color': 'blue', 'width': 2})
        self.main_view.addItem(self.cam_roi)
        self.cam_roi.sigRegionChangeFinished.connect(self.cam_roi_changed)
        self.ui.pushButton_setROI.setEnabled(False)

    def cam_roi_changed(self):
        """
        method of class MainWindow that updates the position of the ROI.
        :return: None
        """
        self.cam_roi_pos = self.cam_roi.pos()
        self.cam_roi_size = self.cam_roi.size()
        x, y, w, h = self.cam_roi_pos[0], self.cam_roi_pos[1], self.cam_roi_size[0], self.cam_roi_size[1]
        self.cam_roi_data = self.image_data[int(
            y):int(y + h), int(x):int(x + w)]

    def apply_ROI(self):
        """
        method of class MainWindow that applies the parameters of the ROI.
        Binning shouldn't be applied excepted for tries
        :return: None
        """
        self.cam_roi_pos = self.cam_roi.pos()
        self.cam_roi_size = self.cam_roi.size()
        x, y, w, h = self.cam_roi_pos[0], self.cam_roi_pos[1], self.cam_roi_size[0], self.cam_roi_size[1]
        self.andor.cam.set_roi(hstart=y, hend=y + h,
                               vstart=x, vend=x + w, hbin=1, vbin=1)
        self.ui.pushButton_apply_ROI.setEnabled(False)
        self.roi_is_applied = True

    def clear_ROI(self):
        """
        method of class MainWindow clears ROI
        :return:
        """
        self.main_view.removeItem(self.cam_roi)
        self.andor.cam.set_roi()
        self.ui.pushButton_setROI.setEnabled(True)
        self.ui.pushButton_apply_ROI.setEnabled(True)
        self.roi_is_applied = False

    def start_acquisition(self):
        initial_directory = "Z:/data_phd_thomas_2023_202x/relaunch_sarocema"
        self.file_path, _ = QFileDialog.getSaveFileName(
            self, "Save NPY File", initial_directory, "NPY Files (*.npy)")
        self.acquistion = True
        self.acquisition_data = []
        self.ui.pushButton_start_acq.setEnabled(False)

    def stop_acquisition(self):
        data = np.array(self.acquisition_data)
        np.save(self.file_path, data)
        self.acquistion = False
        self.acquisition_data = None
        self.ui.pushButton_start_acq.setEnabled(True)

    def on_resize(self, event):
        # Garder la largeur et la hauteur de la fenêtre égales pour le rendre carré
        size = min(self.width(), self.height())
        self.main_view.setGeometry(0, 0, size, size)
        event.accept()
        
    def mouse_click_event(self, event):
        if event.double():
            # Clear existing crosshair
            self.clear_crosshair()
            
            # Get the position of the double click event
            pos = event.pos()
            # Map the position to coordinates of the PlotItem
            pos_mapped = self.main_view.mapSceneToView(pos)
            # Get the x and y coordinates
            self.x_coord = pos_mapped.x()
            self.y_coord = pos_mapped.y()
            
            self.plot_crosshair()
            self.crosshair_enabled = True
                   
    def plot_crosshair(self):
       # Calculate the appropriate size for the crosshair based on the visible range of the plot
        x_range = self.main_view.viewRange()[0]
        y_range = self.main_view.viewRange()[1]

        # Add horizontal line of the crosshair
        self.crosshair_h = pg.PlotCurveItem(x=[x_range[0], x_range[1]], y=[self.y_coord, self.y_coord], pen={'color': 'r', 'width': 1})
        self.main_view.addItem(self.crosshair_h)
        
        # Add vertical line of the crosshair
        self.crosshair_v = pg.PlotCurveItem(x=[self.x_coord, self.x_coord], y=[y_range[0], y_range[1]], pen={'color': 'r', 'width': 1})
        self.main_view.addItem(self.crosshair_v)
        
        # display to the cuts PlotWidgets
        Hcut = self.image_data[:, int(self.y_coord)]
        Vcut = self.image_data[int(self.x_coord), :]
        x_values = np.arange(len(Vcut))
        new_x = Vcut
        new_y = x_values
        self.ui.widget_Hcut.clear()
        self.ui.widget_Vcut.clear()
        self.ui.widget_Hcut.plot(Hcut)
        self.ui.widget_Vcut.plot(new_x, new_y)         
    
    def clear_crosshair(self):
        # Remove existing crosshair
        if self.crosshair_h is not None:
            self.main_view.removeItem(self.crosshair_h)
            self.crosshair_h = None
        if self.crosshair_v is not None:
            self.main_view.removeItem(self.crosshair_v)
            self.crosshair_v = None
        self.crosshair_enabled = False