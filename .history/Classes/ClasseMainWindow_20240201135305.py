
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG)
import matplotlib.pyplot as plt


from Classes.ui_AndorCam import Ui_MainWindow
from Classes.ClasseAndor import AndorCam
from Classes.TrigExtThread import Worker
import pyqtgraph as pg




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.andor = AndorCam()
        self.ui.setupUi(self)
        self._number_frame = 0
        self.worker_thread = None
        self.main_view = self.ui.widgetFrame.addViewBox()
        
        self.normalization_roi = pg.ROI([1024, 1024], [512, 512], pen=pg.mkPen('r', width=2))
        self.main_view.addItem(self.normalization_roi)
        self.normalization_roi_visible = False
        
        self.normalization_roi.setVisible(False)
        self.image_item = 0
        self.position_norm = [0, 0]
        
        # connect buttons with actions
        self.ui.pushButton_shot.clicked.connect(self.display_image_int)
        self.ui.pushButton_start_ext.clicked.connect(self.start_thread)
        self.ui.pushButton_stop_ext.clicked.connect(self.stop_thread)
        self.ui.pushButton_normalisation.clicked.connect(self.toggle_normalization_roi)
        
    def display_image_int(self):  
        self.andor.set_acquisition(acquisition_mode=0, exposure_time=float(self.ui.doubleSpinBox_exposure.value())*1e-3,
                                   trigger_mode='int', frame_method='snap')
        if self.normalization_roi_visible:
            position_norm = [int(coord) for coord in self.normalization_roi.pos()]
            size_norm = [int(coord) for coord in self.normalization_roi.size()]
     
            raw_image = np.array(self.andor.acquisition())
            roi = raw_image[position_norm[1]: position_norm[1]+size_norm[1], position_norm[0]: position_norm[0]+size_norm[0]]
            roi_mean = np.mean(roi)
            normalized_image = raw_image/roi_mean
            print(raw_image,normalized_image)
            self.image_item.setImage(normalized_image)
            plt.figure(1)
            plt.imshow(raw_image)
            plt.figure(2) 
            plt.imshow(normalized_image)   
            plt.show()        
        else:
            image = np.array(self.andor.acquisition())
            self.image_item = pg.ImageItem(image=image)
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
            
    def toggle_normalization_roi(self):
        self.normalization_roi_visible = not self.normalization_roi_visible
        self.normalization_roi.setZValue(int(self.normalization_roi_visible))
        self.normalization_roi.setVisible(self.normalization_roi_visible)
        print(self.position_norm)
        
        if self.normalization_roi_visible:
            self.normalization_roi.setPos(self.position_norm)
            self.normalization_roi.setSize(self.image_item.image.shape)
            
            self.normalization_roi.handleScale = True
            self.normalization_roi.addScaleHandle((0, 0), (1, 1))
            self.normalization_roi.addScaleHandle((1, 1), (0, 0))
            
            self.position_norm = np.array(self.normalization_roi.pos())
            self.size_norm = self.normalization_roi.size()
            
    def close_normalization_ROI(self, event):
        self.position_norm = np.array(self.normalization_roi.pos())
        self.ui.widgetFrame.close()
        event.close()