from threading import Thread

import cv2

import constants


class CVCamera:
    def __init__(self, port, exposure, contrast=7):
        self.camera = cv2.VideoCapture(port)
        self.camera.set(constants.CAMERA_CONTRAST, contrast)
        self.camera.set(constants.CAMERA_EXPOSURE, exposure)
        self.exit = False
        self.frame = None
        print(
            f'Contrast: {contrast} Exposure: {self.camera.get(constants.CAMERA_EXPOSURE)} FPS: {self.camera.get(constants.CAMERA_FPS)}')
        Thread(target=self.loop).start()

    def loop(self):
        while True:
            if self.exit:
                break
            self.frame = self.camera.read()[1]

    def release(self):
        self.exit = True
        self.camera.release()

    def set_exposure(self, exposure):
        self.camera.set(constants.CAMERA_EXPOSURE, exposure)
