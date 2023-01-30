import argparse
import time

from PIL import Image

from cvb_bug.camera import Camera

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Take a image as subprocess.')
    # parser.add_argument('--image_path', help='path where the image should be stored')
    camera = Camera()
    image = camera.take_image()
    print(image)
    # image_obj = Image.fromarray(image)
    # image_obj.save()
