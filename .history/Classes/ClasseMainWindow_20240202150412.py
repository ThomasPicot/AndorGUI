
import pyqtgraph as pg
from Classes.TrigExtThread import Worker
from Classes.ClasseAndor import AndorCam
from Classes.ui_AndorCam import Ui_MainWindow
import matplotlib.pyplot as plt
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
        self.worker_thread = None
        self.roi_norm = None
        self.cam_roi = None
        self.main_view = self.ui.widgetFrame.addViewBox()

        # connect buttons with actions
        self.ui.pushButton_shot.clicked.connect(self.display_image_int)
        self.ui.pushButton_start_ext.clicked.connect(self.start_thread)
        self.ui.pushButton_stop_ext.clicked.connect(self.stop_thread)
        self.ui.pushButton_normalisation.clicked.connect(self.toggle_normalization)

    def display_image_int(self):
        self.andor.set_acquisition(acquisition_mode=0, exposure_time=float(self.ui.doubleSpinBox_exposure.value())*1e-3,
                                   trigger_mode='int', frame_method='snap')
        if self.roi_norm is not None:
            self.image_data = np.array(self.andor.acquisition())
            normalized_image_data = self.image_data / self.roi_norm_mean
            # Update the image item with the normalized data
            self.image_item = pg.ImageItem(image=normalized_image_data)
            self.main_view.addItem(self.image_item)
        else:
            self.image_data = np.array(self.andor.acquisition())
            self.image_item = pg.ImageItem(image=self.image_data)
            self.main_view.addItem(self.image_item)
        self._number_frame = self._number_frame+1
        logging.debug(self._number_frame)

    def display_image_ext(self):
        logging.debug("ext acquisition setting up")
        self.andor.set_acquisition(acquisition_mode=0, exposure_time=float(self.ui.doubleSpinBox_exposure.value())*1e-3,
                                   trigger_mode='ext', frame_method='sequence')
        logging.debug("setup done")
        logging.debug("wating for frame")
        image = np.array(self.andor.acquisition())
        self.image_item = pg.ImageItem(image=image)
        self.main_view.addItem(self.image_item)
        logging.debug("sending image on frame")
        self._number_frame = self._number_frame+1
        logging.debug(self._number_frame)

    def start_thread(self):
        self.worker_trhead = Worker(self)
        self.worker_trhead.start()

    def stop_thread(self):
        if self.worker_trhead is not None and self.worker_trhead.isRunning():
            self.worker_trhead.requestInterruption()
            self.worker_trhead.quit()
            self.worker_trhead.wait(3000)

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
        self.cam_ROI = pg.RectROI([1020, 200], [300, 300], pen={'color': 'blue', 'width': 2})
        self.main_view.addItem(self.cam_roi)
        self.cam_roi.sigRegionChangeFinished.connect(self.cam_roi_changed)

    def cam_roi_changed(self):
        self.cam_roi_pos = self.cam_roi.pos()
        self.cam_roi_size = self.cam_roi.size() 
        x, y, w, h = self.cam_roi_pos[0], self.cam_roi_pos[1], self.cam_roi_size[0], self.cam_roi_size[1]
        self.cam_roi_data = self.image_data[int(y):int(y + h), int(x):int(x + w)]
        
    def apply_ROI(self):
        
        self.andor.cam.set_roi(hstart=, hend=, vstart=, vend=, hbin=2, vbin=2)