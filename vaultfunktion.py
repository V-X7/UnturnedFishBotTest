import cv2 as cv
import numpy as np
import pyautogui
import pywinauto
import pywinauto
import time
from CraftWindowCapture import GetWholeScreenShot
from hsvfilter import HsvFilter
from PIL import Image


from vision import Vision
hitta = Vision("fish14.png")
#hitta.init_control_gui()
guld_ingot_hsv_filter = HsvFilter(19, 77, 174, 26, 155, 205, 0, 0, 0, 0)

def vault(needle):

    threshold = 0.8

    screenshot = GetWholeScreenShot()
    screenshot = screenshot[70:1080, 430:1150]


    if needle == "VaultBilder/goldIngotpaHSV.png":
        hsv = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)

        lower = np.array([guld_ingot_hsv_filter.hMin, guld_ingot_hsv_filter.sMin, guld_ingot_hsv_filter.vMin])
        upper = np.array([guld_ingot_hsv_filter.hMax, guld_ingot_hsv_filter.sMax, guld_ingot_hsv_filter.vMax])
        # Apply the thresholds
        mask = cv.inRange(hsv, lower, upper)
        mask_ = Image.fromarray(mask)
        result = cv.bitwise_and(hsv, hsv, mask=mask)

        screenshot = cv.cvtColor(result, cv.COLOR_HSV2BGR)



    needle = cv.imread(needle, cv.IMREAD_UNCHANGED)
    needle_w = needle.shape[1]
    needle_h = needle.shape[0]
    needle = cv.cvtColor(needle, cv.COLOR_RGBA2RGB)



    result = cv.matchTemplate(screenshot, needle, cv.TM_CCOEFF_NORMED)

    # Get the all the positions from the match result that exceed our threshold
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    # print(locations)

    # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
    # locations by using groupRectangles().
    # First we need to create the list of [x, y, w, h] rectangles
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)
        rectangles.append(rect)
    # Apply group rectangles.
    # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
    # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
    # in the result. I've set eps to 0.5, which is:
    # "Relative difference between sides of the rectangles to merge them into a group."
    rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)




    points = []
    if len(rectangles):
        # print('Found needle.')

        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:

            # Determine the center position
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            pyautogui.keyDown('ctrl')
            pywinauto.mouse.move(coords=((center_x + 430), (center_y + 70)))
            time.sleep(0.05)
            pyautogui.click(button="right")
            pyautogui.keyUp('ctrl')
            # Save the points
            points.append((center_x, center_y))

                # Determine the box position
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # Draw the box
            cv.rectangle(screenshot, top_left, bottom_right, color=line_color,
                         lineType=line_type, thickness=2)





        # cv.imwrite('result_click_point.jpg', screenshot)

    return points
