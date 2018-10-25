import cv2

import utils
from display import Display
from trackbars import Trackbars

name = "target"
target = __import__(name).Target(name)

display = Display()
trackbars = Trackbars(name)

while True:
    frame = display.get_frame()
    # Seperate frames for display purposes
    original = frame.copy()
    contour_image = frame.copy()
    # Target functions
    mask = target.create_mask(frame)
    contours = target.find_contours(mask)
    filtered_contours = target.filter_contours(contours)
    # Draw contours
    target.draw_contours(filtered_contours, contour_image)
    # Display
    display.show_frame(contour_image)
    display.show_frame(utils.bitwise_mask(original, mask), title="mask")
    k = cv2.waitKey(1) & 0xFF  # large wait time to remove freezing
    if k in (27, 113):
        break
