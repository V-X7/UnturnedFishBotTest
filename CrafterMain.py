import cv2 as cv
import numpy as np
import os
from CraftWindowCapture import GetScreenShot
from CrafterVision import find
import time

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each videqqo in their own folder on GitHub
#os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
#wincap = GetScreenShot('Unturned')
# initialize the Vision class

loop_time = time.time()
time.sleep(3)
while(True):

    # get an updated image of the game
    screenshot = GetScreenShot()
    #cv.imshow('screenshot', screenshot)
    #edgeScreen = cv.Canny(screenshot, 100, 200)
    # display the processed image
    #screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2GRAY)
    '''hej = cv.imread("silverToGold.png")
    cv.imshow('screenshot', screenshot)
    cv.imshow('screasdasdasd', hej)'''

    find(screenshot, "silverToGold.png", 0.65, 'rectangles')
    time.sleep(0.1)
    find(screenshot, "CoinsToNuggets.png", 0.65, 'rectangles')
    time.sleep(0.1)
    find(screenshot, "NuggetsToIngots.png", 0.65, 'rectangles')
    break


    # debug the loop rate
    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')