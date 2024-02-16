from PyQt5.QtCore import QThread, pyqtSignal, QMutexLocker, QMutex
from numpy import ndarray
import logging
logging.basicConfig(level=logging.DEBUG)

class Worker(QThread):
    data_processed = pyqtSignal(ndarray)
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.mutex = QMutex()
        
        
    def run(self):
        try:
            while True:
                logging.debug("thread is running...")
                locker = QMutexLocker(self.mutex)
                if self.isInterruptionRequested():   
                    locker.unlock()
                    logging.debug("thread interrupted")
                    break
                locker.unlock()
                
                self.window.display_image_ext()
                logging.debug("function executed")
                if self.isInterruptionRequested():
                    logging.debug("Thread interrupted after function execution")
                    break
        except Exception as e:
            logging.exception(f"Exception in thread: {str(e)}")   
        