from PyQt5.QtCore import QThread
import logging

logging.basicConfig(level=logging.DEBUG)


class Worker(QThread):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def run(self):
        try:
            while True:

                # Perform your thread's operation here
                self.window.display_image_ext()

                # Check for thread interruption request
                if self.isInterruptionRequested():

                    break
        except Exception as e:
            logging.exception(f"Exception in thread: {str(e)}")
