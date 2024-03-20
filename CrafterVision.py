import time

import cv2 as cv
import numpy as np
import pywinauto
import pyautogui



def find(haystack_img, needle_img, threshold=0.7, debug_mode=None):
    # run the OpenCV algorithm


    needle_img = cv.imread(needle_img, cv.IMREAD_UNCHANGED)
    method = cv.TM_CCOEFF_NORMED
    # Save the dimensions of the needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    # There are 6 methods to choose from:
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED



    result = cv.matchTemplate(haystack_img, needle_img, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if max_val >= threshold:
        print("Klickade på dessa coordinater:" + str(max_loc[0]) + ", " + str(max_loc[1]) + "och detta var värdet" + str(max_val) + "\n")
        pywinauto.mouse.move(coords=(max_loc[0], max_loc[1]+30))
        time.sleep(0.1)
        pyautogui.keyDown('ctrl')
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.keyUp('ctrl')
    else:
        print(str(max_val) + "\n")



