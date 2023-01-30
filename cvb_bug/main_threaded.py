import sys

from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QApplication

from cvb_bug.camera import Camera
from cvb_bug.runner import Runner, Generation


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.threadpool = None
        self.runner = None

        layout = QVBoxLayout()

        btn_gen2 = QPushButton("Start Gen2")
        btn_gen2.pressed.connect(self.start_gen2)

        btn_gen3 = QPushButton("Start Gen3")
        btn_gen3.pressed.connect(self.start_gen3)

        layout.addWidget(btn_gen2)
        layout.addWidget(btn_gen3)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.show()

    def start_gen2(self):
        print("START")
        self.threadpool = QThreadPool()
        self.runner = Runner(Generation.GENTWO)
        self.threadpool.start(self.runner)

    def start_gen3(self):
        print("START")
        self.threadpool = QThreadPool()
        self.runner = Runner(Generation.GENTHREE)
        self.threadpool.start(self.runner)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
