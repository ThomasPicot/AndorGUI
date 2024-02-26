import pylablib as pll
import numpy as np
import pyqtgraph as pg
from pylablib.devices import Andor


class AndorCam:
    def __init__(self, SDK_path: str = "D:\SDKs\Andor\Andor") -> None:
        """
        Initiate the object cam that takes all the attributes of the camera Andor
        :param SDK_path:path to the andor SDK file.
        """
        pll.par["devices/dlls/andor_sdk3"] = SDK_path
        self.cam = Andor.AndorSDK3Camera()  # initiate the object Andor
        self.exposure_time = 0
        self.trigger_mode = 0
        self.frame_method = 0
        self.fps = 0

    def set_acquisition(self, acquisition_mode: float, exposure_time: float, trigger_mode: str, frame_method: str,
                        fps: float = 1):
        """
        class method of AndorCam that setup the acquisition with the parameters entered.
        :param exposure_time: time in [ms] of exposure
        :param trigger_mode: 'ext' when using the GoodTime sequences, 'int' when just taking a picture
        :param frame_method: can be 'snap' for just one picture or 'sequence' when using GoodTime sequences
        :param fps: frame per seconds. For fluoresence 1 is enough
        :return: None
        """
        self.cam.clear_acquisition()
        self.acquisition_mode = acquisition_mode
        self.exposure_time = exposure_time
        self.trigger_mode = trigger_mode
        self.frame_method = frame_method
        self.fps = fps
        self.cam.set_exposure(self.exposure_time)
        self.cam.set_trigger_mode(mode=self.trigger_mode)
        self.cam.set_frame_period(self.fps)

    def acquisition(self):
        """
        class method of AndorCam that starts the acquisition, stores all the images in image and
        stops the acquisition.
        NB: most of the time there is only one image in the array as I use it in MainWindow.
        :return: an array of images
        """
        self.cam.start_acquisition()
        self.cam.wait_for_frame(timeout=1e10)
        image = self.cam.read_newest_image()
        self.cam.stop_acquisition()
        return image

    def get_statu_cam(self):
        """
        class method of AndorCam that gets the statues of the camera Andor such that the temperature
        and return a list of all the data as strings
        :return:
        """
        return self.cam.get_all_attribute_values()
