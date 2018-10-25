import json
import os

import cv2
import numpy as np

default = {"H": (0, 255), "S": (0, 255), "V": (0, 255)}


def get_filename(name):
    return "hsv/{}.json".format(name)


def save_file(name, hsv):
    with open(get_filename(name), "w") as f:
        json.dump(hsv, f)


def load_file(name):
    if not os.path.isfile(get_filename(name)):
        save_file(name, default)
    with open(get_filename(name), "r") as f:
        return json.load(f)


def aspect_ratio(cnt):
    rect = cv2.minAreaRect(cnt)
    width = rect[1][0]
    height = rect[1][1]
    return width / height


def hsv_mask(frame, hsv):
    hsv_colors = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([hsv["H"][0], hsv["S"][0], hsv["V"][0]])
    higher_hsv = np.array([hsv["H"][1], hsv["S"][1], hsv["V"][1]])
    mask = cv2.inRange(hsv_colors, lower_hsv, higher_hsv)
    return mask


def morphology(mask, kernel):
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return mask


def bitwise_mask(frame, mask):
    frame = frame.copy()
    return cv2.bitwise_and(frame, frame, mask=mask)
