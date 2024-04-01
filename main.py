import cv2 as cv
import numpy as np
import time
import pyautogui
import win32gui, win32ui, win32con
from WindowCapture import GetScreenShot
from vision import Vision
from hsvfilter import HsvFilter
from Sell import sälja
from PIL import ImageOps
from PIL import Image
from vaultfunktion import vault
from CrafterVision import craft
from Drop import drop
from CraftWindowCapture import GetWholeScreenShot
import EasyOCR
from EasyOCR import CraftOCR
'''
lägg till en setup som ser till att hide uncraftablde blueprints är på och att scrollen är helt rätt
'''
hitta = Vision("fish14.png")
loop_time = time.time()
sälj_tid = time.time()
vault_tid = time.time()
craft_tid = time.time()
drop_tid = time.time()
#hitta.init_control_gui()
hsv_filter_for_gold_text = HsvFilter(0,0,119,138,8,255,0,0,0,0)

hsv_filter = HsvFilter(73, 50,0,117,255,255,0,0,0,0)
guld_ingot_hsv_filter = HsvFilter(19, 77, 174, 26, 155, 205, 0, 0, 0, 0)



time.sleep(3)
pyautogui.mouseDown()
time.sleep(1.9)
pyautogui.mouseUp()
time.sleep(5)


while True:
    screenshot = GetScreenShot()

    screenshot = cv.bitwise_not(screenshot)

    output_image = hitta.apply_hsv_filter(screenshot, hsv_filter)

    #hitta.find(output_image, 0.75, "rectangles", 1)
    #cv.imshow("screenshot", output_image)

    print("Fps {}".format(1/(time.time()- loop_time)))
    loop_time = time.time()
    #cv.imshow("stream", screenshot)



   #Körr sell py efter l¨ång tid
    if (sälj_tid + 240) < time.time():
        pyautogui.click()
        sälja()
        sälj_tid = time.time()
        now = time.ctime(int(time.time()))
        print("Sålde fiskarna klockan " + str(now))

    if (drop_tid + 480) < time.time():
        pyautogui.click()
        pyautogui.press("tab")
        time.sleep(0.2)
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

        drop_tid = time.time()
        now = time.ctime(int(time.time()))
        print("droppade saker klockan " + str(now))
        pyautogui.press("esc")
        pyautogui.mouseDown()
        time.sleep(1.9)
        pyautogui.mouseUp()
        time.sleep(5)

    if (craft_tid + 720) < time.time():
        pyautogui.click()
        pyautogui.press("y")
        CraftOCR("silverToGold")
        CraftOCR("CoinsToNugget")
        CraftOCR("NuggetToIngot")
        CraftOCR("polarisRoseBox")
        CraftOCR("cyanCrystalBox")
        CraftOCR("CopperCoil")
        CraftOCR("CopperStack")
        CraftOCR("tape")

        craft_tid = time.time()
        now = time.ctime(int(time.time()))
        print("Craftade saker klockan " + str(now))
        pyautogui.press("esc")
        pyautogui.mouseDown()
        time.sleep(1.9)
        pyautogui.mouseUp()
        time.sleep(5)

    if (vault_tid + 1440) < time.time():

        pyautogui.click()

        pyautogui.press("enter")
        time.sleep(0.1)
        pyautogui.write("/vault")
        pyautogui.press("enter")
        time.sleep(0.2)

        vault("VaultBilder/goldIngotpaHSV.png")
        vault("VaultBilder/PolarisRoseBoxIconCropped.png")
        vault("VaultBilder/cyanCrystalBoxIconCropped.png")
        
        for x in range(30):
            pyautogui.scroll(-1)
        vault("VaultBilder/goldIngotpaHSV.png")
        vault("VaultBilder/PolarisRoseBoxIconCropped.png")
        vault("VaultBilder/cyanCrystalBoxIconCropped.png")
        for x in range(30):
            pyautogui.scroll(1)

        vault_tid = time.time()
        now = time.ctime(int(time.time()))
        print("Vaultade saker klockan " + str(now))
        pyautogui.press("esc")
        pyautogui.mouseDown()
        time.sleep(1.9)
        pyautogui.mouseUp()
        time.sleep(5)



    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break

print("Done")