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
'''
Ist'älelt fär att kära match template en gång till klåte loopen köra en gång opch om den kommer in i debn kloopen igen så kan det dra i spöet

Så första gågen den kommer in loopen så höjer den en counter, om de6t  jhänder två gånger iorad så drar den in spöet, om det inte händer två gånger irad så sätter cen counter till noll
'''
hitta = Vision("fish14.png")
loop_time = time.time()
fisk_tid = time.time()
#hitta.init_control_gui()

hsv_filter = HsvFilter(73, 50,0,117,255,255,0,0,0,0)

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
    cv.imshow("screenshot", output_image)

    print("Fps {}".format(1/(time.time()- loop_time)))
    loop_time = time.time()
    #cv.imshow("stream", screenshot)



   #Körr sell py efter l¨ång tid
    if (fisk_tid + 600) < time.time():
        sälja()
        fisk_tid = time.time()



    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break

print("Done")