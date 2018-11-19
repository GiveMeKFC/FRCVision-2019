from abc import ABC, abstractmethod

import cv2
import numpy as np

import utils


class TargetBase(ABC):
    """An abstract class representing a base target."""

    @staticmethod
    def create_mask(frame, hsv):
        """
        :param frame: the frame to process
        :param hsv: JSON file
        :return: the mask of the target
        """
        mask = utils.hsv_mask(frame, hsv)
        # create a cross kernel
        mask = utils.morphology(mask, np.array([[0, 1, 0],
                                                [1, 1, 1],
                                                [0, 1, 0]], dtype=np.uint8))
        mask = cv2.threshold(mask, 127, 255, 0)[1]
        return mask

    @classmethod
    def find_contours(cls, mask) -> list:
        """
        :param mask: mask of the target
        :return: list of contours in the mask
        """
        return cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]

    @classmethod
    @abstractmethod
    def filter_contours(cls, contours: list):
        """
        Filter the contours of the target.
        :param contours: list of contours
        """
        pass

    @classmethod
    @abstractmethod
    def draw_contours(cls, filtered_contours: list, contour_image):
        """
        Draw the contours on the frame.
        :param filtered_contours: filtered contours of the mask
        :param contour_image: frame the contours were found it
        """
        pass
