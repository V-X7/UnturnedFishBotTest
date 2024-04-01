import easyocr
import cv2 as cv
import matplotlib.pyplot as plt
import time
import cv2 as cv
import numpy as np
import pywinauto
import pyautogui
from hsvfilter import HsvFilter
hsv_filter_for_gold_text = HsvFilter(0,0,119,138,8,255,0,0,0,0)
from CraftWindowCapture import GetWholeScreenShot
from vision import Vision
from thefuzz import fuzz
'''
Plan för detta, i if detmansoker
Lägg till en string från text searchen, Kör fuzzy match på den, ha ett confidence threshold på det 
'''

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



def CraftOCR(detmansoker):
    time.sleep(0.2)



    if detmansoker == "silverToGold":
        searchString = "Silver Coins 5/4 = Gold Coins xl"
        gold()
    if detmansoker == "CoinsToNugget":
        searchString ="Gold Coins 5/5 = Gold Nugget xl"
        gold()
    if detmansoker == "NuggetToIngot":
        searchString ="Gold Nugget 5/5 = Gold Ingot xl"
        gold()
    if detmansoker == "polarisRoseBox":
        searchString ="Polaris Rose 10/10 = Box_of_Polaris_Rose xl"
        polaris_rose()
    if detmansoker == "cyanCrystalBox":
        cyan_crystal()
        searchString ="Cyan Crystal 10/10 = Box_of_Cyan_Crystal xl"
    if detmansoker == "CopperStack":
        copperStack()
        searchString ="Industrial Copper Coil 10/10 = Stack_of_Industrial_Coil xl"
    if detmansoker == "CopperCoil":
        copperCoil()
        searchString ="Copper Coil 4/4 = Industrial Copper Coil xl"
    if detmansoker == "tape":
        tape()
        searchString ="Tape 10/10 = Stack of tape xl"

    haystack_img = GetWholeScreenShot()

    x0 = 730
    y0 = 130
    x1 = 1170
    y1 = 840
    haystack_img = haystack_img[y0:y1, x0:x1]


    reader = easyocr.Reader(["en"], gpu=True)

    text_ = reader.readtext(haystack_img, paragraph=True, decoder="greedy")


    score = []
    for t in text_:
        text_, score_ = t
        #print(score_)
        score.append(score_)
        score.append(text_)

    for x in score:
        if fuzz.ratio(searchString, str(x)) > 85:
            top_left = score[(score.index(x)+1)][0]
            xClick = top_left[0] + x0
            yClick = top_left[1] + y0



            time.sleep(0.1)
            pyautogui.keyDown('ctrl')
            time.sleep(0.1)
            pyautogui.moveTo(xClick, yClick)
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.keyUp('ctrl')
            print("Klickade på dessa coordinater:" + str(xClick) + ", " + str(yClick) +" och jag craftade " + str(x) + " med säkerheten " + str(fuzz.ratio(searchString, str(x))))
            break
