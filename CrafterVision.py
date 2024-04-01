import time
import cv2 as cv
import numpy as np
import pywinauto
import pyautogui
from hsvfilter import HsvFilter
hsv_filter_for_gold_text = HsvFilter(0,0,119,138,8,255,0,0,0,0)
from CraftWindowCapture import GetWholeScreenShot
from vision import Vision


def polaris_rose():
    pywinauto.mouse.move(coords=((916, 158)))
    pyautogui.click()
    pyautogui.write("Box_of_Polaris_Rose")
    pyautogui.press("enter")
    time.sleep(0.1)

def cyan_crystal():
    pywinauto.mouse.move(coords=((916, 158)))
    pyautogui.click()
    pyautogui.write("Cyan crystal")
    pyautogui.press("enter")
    time.sleep(0.1)

def gold():
    pywinauto.mouse.move(coords=((916, 158)))
    pyautogui.click()
    pyautogui.write("gold")
    pyautogui.press("enter")
    time.sleep(0.1)
def copperStack():
    pywinauto.mouse.move(coords=((916, 158)))
    pyautogui.click()
    pyautogui.write("Stack_of_Industrial_Coil")
    pyautogui.press("enter")
    time.sleep(0.1)
def copperCoil():
    pywinauto.mouse.move(coords=((916, 158)))
    pyautogui.click()
    pyautogui.write("Copper Coil")
    pyautogui.press("enter")
    time.sleep(0.1)

def tape():
    pywinauto.mouse.move(coords=((916, 158)))
    pyautogui.click()
    pyautogui.write("stack of tape")
    pyautogui.press("enter")
    time.sleep(0.1)

def craft(detmansoker, threshold=0.2):
    time.sleep(0.2)
    haystack_img = GetWholeScreenShot()
    '''
    hsv = cv.cvtColor(haystack_img, cv.COLOR_BGR2HSV)

    lower = np.array([hsv_filter.hMin, hsv_filter.sMin, hsv_filter.vMin])
    upper = np.array([hsv_filter.hMax, hsv_filter.sMax, hsv_filter.vMax])
    # Apply the thresholds
    haystack_img = cv.inRange(hsv, lower, upper)
    #cv.imread(haystack_img, 0)
    cv.imwrite("JagSerDetHSV.png", haystack_img)

        '''

    x0 = 730
    y0 = 130
    x1 = 1170
    y1 = 840
    haystack_img = haystack_img[y0:y1, x0:x1]

    # run the OpenCV algorithm

    time.sleep(0.5)
    if detmansoker == "silverToGold":
        needle_img = "CraftBilder/silverToGold.png"
        gold()
    if detmansoker == "CoinsToNugget":
        needle_img = "CraftBilder/CoinsToNuggetsV3.png"
        gold()
    if detmansoker == "NuggetToIngot":
        needle_img = "CraftBilder/NuggetToIngotV2.png"
        gold()
    if detmansoker == "polarisRoseBox":
        needle_img = "CraftBilder/polarisRoseBox.png"
        polaris_rose()
    if detmansoker == "cyanCrystalBox":
        needle_img = "CraftBilder/cyanCrystalBox.png"
        cyan_crystal()

    if detmansoker == "CopperStack":
        needle_img = "CraftBilder/Cropped copper stack of industrial.png"
        copperStack()
    if detmansoker == "CopperCoil":
        needle_img = "CraftBilder/CopperCoil.png"
        copperCoil()
    if detmansoker == "tape":
        needle_img = "CraftBilder/stackOfTape.png"
        tape()
    needle_img = cv.imread(needle_img, cv.IMREAD_UNCHANGED)
    needle_img = cv.cvtColor(needle_img, cv.COLOR_RGBA2RGB)


    #needle_img = cv.inRange(hsv, lower, upper)

    method = cv.TM_CCORR_NORMED

    # Save the dimensions of the needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    # There are 6 methods to choose from:
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED


    result = cv.matchTemplate(haystack_img, needle_img, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if max_val >= threshold:



        print("Klickade på dessa coordinater:" + str(max_loc[0] + int((needle_w/2)) + 830 )  + ", " + str(max_loc[1] + int((needle_h/2)) + 130 ) + "och detta var värdet" + str(max_val) + "\n")
        time.sleep(0.1)
        pyautogui.keyDown('ctrl')
        time.sleep(0.1)
        pywinauto.mouse.move(coords=((max_loc[0] + int((needle_w/2)) + 830), (max_loc[1]+ int((needle_h/2)) + 130)))
        time.sleep(0.1)
        #pyautogui.click()
        time.sleep(0.1)
        pyautogui.keyUp('ctrl')
    else:
        print(str(max_val) + "\n")


