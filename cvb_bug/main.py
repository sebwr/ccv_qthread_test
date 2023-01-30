import time

from cvb_bug.camera import Camera

if __name__ == "__main__":
    camera = Camera()
    for x in range(5):
        image = camera.take_image()
        print(image.shape)
        time.sleep(0.5)
    del camera
