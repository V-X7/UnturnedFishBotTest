import cv2
import cv2 as cv
import numpy as np
import os
from CraftWindowCapture import GetWholeScreenShot
import time
from hsvfilter import HsvFilter
from CrafterVision import craft
from vision import Vision
from Drop import drop
import pyautogui
from vaultfunktion import vault
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each videqqo in their own folder on GitHub
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
from EasyOCR import CraftOCR
#hitta = Vision("fish14.png")
# initialize the WindowCapture class
#wincap = GetWholeScreenShot('Unturned')
# initialize the Vision class
hsv_filter_for_gold_text = HsvFilter(0,0,119,138,8,255,0,0,0,0)
guld_ingot_hsv_filter = HsvFilter(19, 77, 174, 26, 155, 205, 0, 0, 0, 0)
#hitta.init_control_gui()
loop_time = time.time()
#Koordinat för sökfält är (720, 158)

'''
#stycket här är för att droppa alla saker och scrolla
time.sleep(2)
pyautogui.press("tab")
time.sleep(0.1)
screenshot = GetWholeScreenShot()
drop(screenshot, "DropBilder/brokenGasmaskCrop.png")
drop(screenshot, "DropBilder/benedictPenguinCrop.png")
drop(screenshot, "DropBilder/cottonWoolCrop.png")
drop(screenshot, "DropBilder/militaryDriveCrop.png")
for x in range(30):
    pyautogui.scroll(-1)

time.sleep(0.1)

screenshot = GetWholeScreenShot()
drop(screenshot, "DropBilder/brokenGasmaskCrop.png")
drop(screenshot, "DropBilder/benedictPenguinCrop.png")
drop(screenshot, "DropBilder/cottonWoolCrop.png")
drop(screenshot, "DropBilder/militaryDriveCrop.png")
for x in range(30):
    pyautogui.scroll(1)

time.sleep(3)
pyautogui.press("y")

craft("silverToGold")
craft("CoinsToNugget")
craft("NuggetToIngot")
craft("polarisRoseBox")
craft("cyanCrystalBox")
craft("CopperCoil")
craft("CopperStack")
craft("tape")

pyautogui.press("y")
pyautogui.mouseDown()
time.sleep(1.9)
pyautogui.mouseUp()
time.sleep(5)


time.sleep(3)
vault()
'''
time.sleep(3)
pyautogui.press("y")

CraftOCR("silverToGold")
CraftOCR("CoinsToNugget")
CraftOCR("NuggetToIngot")
CraftOCR("polarisRoseBox")
CraftOCR("cyanCrystalBox")
CraftOCR("CopperCoil")
CraftOCR("CopperStack")
CraftOCR("tape")

'''
hitta = Vision("fish14.png")

hitta.init_control_gui()
while(True):

    # get an updated image of the game
    #screenshot = cv.imread("StoraBilder/allt loot bild.png", cv.IMREAD_UNCHANGED)
    screenshot = GetWholeScreenShot()

    hsvscreenshot = hitta.apply_hsv_filter(screenshot)

    cv.imshow("hj", hsvscreenshot)

    


    # debug the loop rate
    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
'''