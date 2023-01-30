import subprocess
import time

from PySide6.QtCore import QRunnable, Slot


class RunnerSubprocess(QRunnable):
    @Slot()
    def run(self) -> None:
        try:
            for x in range(5):
                print(f"Run {x}")
                output = subprocess.check_output("python subprocess_script.py", shell=True)
                print(output)
                time.sleep(0.5)
        except Exception as e:
            print(e)

