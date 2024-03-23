import cv2 as cv
import numpy as np
import os
from CraftWindowCapture import GetScreenShot
from CrafterVision import find
import time
from hsvfilter import HsvFilter
from CrafterVision import find
from vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each videqqo in their own folder on GitHub
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

hitta = Vision("fish14.png")
# initialize the WindowCapture class
#wincap = GetScreenShot('Unturned')
# initialize the Vision class
hsv_filter_for_gold_text = HsvFilter(0,0,119,138,8,255,0,0,0,0)
hitta.init_control_gui()
loop_time = time.time()
time.sleep(3)
#Koordinat för sökfält är (720, 158)
while(True):

    # get an updated image of the game
    #screenshot = GetScreenShot()
    screenshot = cv.imread("allt loot bild.png", cv.IMREAD_UNCHANGED)
    hsvscreenshot = hitta.apply_hsv_filter(screenshot)

    cv.imshow("hj", hsvscreenshot)


    '''
    find(screenshot, "silverToGold.png", 0.65, 'rectangles')
    find(screenshot, "CoinsToNuggets.png", 0.65, 'rectangles')
    find(screenshot, "NuggetsToIngots.png", 0.65, 'rectangles')
    '''


    # debug the loop rate
    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')