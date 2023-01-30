from pathlib import Path

import cvb
import numpy as np


class Camera:
    """
    Class which holds the logic of the camera. Since there is currently only on type of camera deployed the path to
    the driver is hardcoded and set to port 0
    """

    def __init__(self):
        self.camera_path = str(Path(cvb.install_path()) / "drivers" / "GenICam.vin")

    def take_image_gen2(self) -> np.array:
        with cvb.DeviceFactory.open(self.camera_path, port=0) as device:
            stream = device.stream()
            stream.start()
            image, status = stream.wait()
            with image:
                taken_image = cvb.as_array(image, copy=True)
                print(taken_image.flags["OWNDATA"])
                print(taken_image.shape)
            stream.abort()
            return taken_image

    @staticmethod
    def take_image_gen3() -> np.array:
        devices = cvb.DeviceFactory.discover_from_root(cvb.DiscoverFlags.IgnoreVins)
        with cvb.DeviceFactory.open(devices[0].access_token, cvb.AcquisitionStack.GenTL) as device:
            stream = device.stream(cvb.ImageStream)
            stream.start()
            image, status, node_maps = stream.wait()
            with image:
                taken_image = cvb.as_array(image, copy=True)
                print(taken_image.flags["OWNDATA"])
                print(taken_image.shape)
            stream.abort()
            return taken_image

