import time
from enum import Enum, auto

from PySide6.QtCore import QRunnable, Slot, Signal, QObject

from cvb_bug.camera import Camera


class Generation(Enum):
    GENTWO = auto()
    GENTHREE = auto()


class Runner(QRunnable):

    def __init__(self, generation: Generation):
        super().__init__()
        self.__generation = generation
        self.__camera_instance: Camera = Camera()

    @Slot()
    def run(self) -> None:
        for x in range(5):
            if self.__generation == Generation.GENTWO:
                self.__camera_instance.take_image_gen2()
            elif self.__generation == Generation.GENTHREE:
                self.__camera_instance.take_image_gen3()
            time.sleep(0.5)
