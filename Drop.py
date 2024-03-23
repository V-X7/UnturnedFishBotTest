import time
import cv2 as cv
import numpy as np
import pywinauto
import pyautogui


def drop(haystack_img,needle_img,  threshold=0.7):
    # run the OpenCV algorithm
    #Saker som ska droppas: Broken gasmask, military drive, benedict penguin, Cotton wool

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
        bottom = ((max_loc[0]+needle_w), (max_loc[1]+needle_h))
        cv.rectangle(haystack_img, max_loc, bottom, (0, 255, 0), 5, )
        cv.imshow("stram", haystack_img)

        '''
        print("Klickade på dessa coordinater:" + str(max_loc[0]) + ", " + str(max_loc[1]) + "och detta var värdet" + str(max_val) + "\n")
        time.sleep(0.1)
        pyautogui.keyDown('ctrl')
        time.sleep(0.1)
        pywinauto.mouse.move(coords=(max_loc[0], max_loc[1]+30))
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.keyUp('ctrl')
    else:
        print(str(max_val) + "\n")
    pyautogui.click("esc")
    pyautogui.mouseDown()
    time.sleep(1.9)
    pyautogui.mouseUp()
    time.sleep(5)




'''