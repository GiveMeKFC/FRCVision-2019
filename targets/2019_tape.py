import cv2

import utils
from targets.target_base import TargetBase


class Target(TargetBase):
    """The 2019 Slanted light reflection tape."""

    def __init__(self):
        super().__init__()
        self.exposure = -20

    @staticmethod
    def filter_contours(contours, hierarchy):
        correct_contours = []
        for cnt in contours:
            if len(cnt) < 20 or cv2.contourArea(cnt) < 50:
                continue
            if utils.approx_poly(cnt) == 4:
                print(cv2.contourArea(cnt))
                correct_contours.append(cnt)
        return correct_contours

    @staticmethod
    def draw_contours(filtered_contours, original):
        if not filtered_contours:
            return
        cv2.drawContours(original, filtered_contours, -1, (0, 255, 0), 3)
