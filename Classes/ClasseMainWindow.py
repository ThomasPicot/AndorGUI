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
        
        # __________________________________________________________________________
        # connect buttons with methods
        # __________________________________________________________________________
        
        # acquisition part _________________________________________________________
        self.ui.pushButton_shot.clicked.connect(self.display_image_int)
        self.ui.pushButton_start_ext.clicked.connect(self.start_thread)
        self.ui.pushButton_stop_ext.clicked.connect(self.stop_thread)
        self.ui.pushButton_normalisation.clicked.connect(self.toggle_normalization)
        self.ui.pushButton_setROI.clicked.connect(self.set_ROI)
        self.ui.pushButton_apply_ROI.clicked.connect(self.apply_ROI)
        self.ui.pushButton_clear_ROI.clicked.connect(self.clear_ROI)
        
        # saving data part _________________________________________________________
        self.ui.pushButton_start_acq.clicked.connect(self.start_acquisition)
        self.ui.pushButton_stop_acq.clicked.connect(self.stop_acquisition)

    def display_image_int(self):
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
        self._number_frame += 1
        self.ui.textBrowserLogs.clear()
        self.ui.textBrowserLogs.append("Frame number : "+str(self._number_frame))

    def display_image_ext(self):
        
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
        #self.ui.textBrowserLogs.clear()
        self.ui.textBrowserLogs.append("Frame number : "+str(self._number_frame))
        if self.acquistion is True:
            self.acquisition_data.append(self.image_data)

    def start_thread(self):
        self.worker_thread = Worker(self)
        self.worker_thread.start()
        self._number_frame = 0
        self.main_view.clear()


    def stop_thread(self):
        if self.worker_thread is not None and self.worker_thread.isRunning():
            self.worker_thread.requestInterruption()
            self.ui.textBrowserLogs.append("Stopping thread")
            self.worker_thread.wait(1000)
            self.worker_thread.quit()
            self._number_frame = 0

    def toggle_normalization(self):
        if self.roi_norm is None:
            # Create ROI the first time the button is clicked
            self.roi_norm = pg.RectROI([1020, 1020], [300, 300], pen=(0, 9))
            self.main_view.addItem(self.roi_norm)
            self.roi_norm.sigRegionChangeFinished.connect(self.roi_norm_changed)
        else:
            # Toggle ROI visibility
            self.roi_norm.setVisible(not self.roi_norm.isVisible())
            self.roi_norm = None

    def roi_norm_changed(self):
        self.roi_norm_pos = self.roi_norm.pos()
        self.roi_norm_size = self.roi_norm.size()
        # Extract the region within the ROI
        x, y, w, h = self.roi_norm_pos[0], self.roi_norm_pos[1], self.roi_norm_size[0], self.roi_norm_size[1]
        self.roi_norm_data = self.image_data[int(y):int(y + h), int(x):int(x + w)]

        # Calculate the mean of all points within the ROI
        self.roi_norm_mean = np.mean(self.roi_norm_data)

        # Divide the entire image by the mean of the ROI
        normalized_image_data = self.image_data / self.roi_norm_mean
        # Update the image item with the normalized data
        self.image_item = pg.ImageItem(image=normalized_image_data)
        self.main_view.addItem(self.image_item)

    def set_ROI(self):
        self.cam_roi = pg.RectROI([1020, 200], [300, 300], pen={'color': 'blue', 'width': 2})
        self.main_view.addItem(self.cam_roi)
        self.cam_roi.sigRegionChangeFinished.connect(self.cam_roi_changed)
        self.ui.pushButton_setROI.setEnabled(False)

    def cam_roi_changed(self):
        self.cam_roi_pos = self.cam_roi.pos()
        self.cam_roi_size = self.cam_roi.size()
        x, y, w, h = self.cam_roi_pos[0], self.cam_roi_pos[1], self.cam_roi_size[0], self.cam_roi_size[1]
        self.cam_roi_data = self.image_data[int(y):int(y + h), int(x):int(x + w)]

    def apply_ROI(self):
        self.cam_roi_pos = self.cam_roi.pos()
        self.cam_roi_size = self.cam_roi.size()
        x, y, w, h = self.cam_roi_pos[0], self.cam_roi_pos[1], self.cam_roi_size[0], self.cam_roi_size[1]
        self.andor.cam.set_roi(hstart=y, hend=y + h, vstart=x, vend=x + w, hbin=1, vbin=1)
        self.ui.pushButton_apply_ROI.setEnabled(False)

    def clear_ROI(self):
        self.main_view.removeItem(self.cam_roi)
        self.andor.cam.set_roi()
        self.ui.pushButton_setROI.setEnabled(True)
        self.ui.pushButton_apply_ROI.setEnabled(True)

    def start_acquisition(self):
        initial_directory = "Z:/data_phd_thomas_2023_202x/relaunch_sarocema"
        self.file_path, _ = QFileDialog.getSaveFileName(self, "Save NPY File", initial_directory, "NPY Files (*.npy)")
        self.acquistion = True
        self.acquisition_data = []
        self.ui.pushButton_start_acq.setEnabled(False)

    def stop_acquisition(self):
        data = np.array(self.acquisition_data)
        np.save(self.file_path, data)
        self.acquistion = False
        self.acquisition_data = None
        self.ui.pushButton_start_acq.setEnabled(True)
