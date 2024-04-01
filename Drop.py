import time
import cv2 as cv
import numpy as np
import pywinauto
import pyautogui
from hsvfilter import HsvFilter

def drop(haystack_img,needle_img, threshold=0.95):
    # run the OpenCV algorithm
    #Saker som ska droppas: Broken gasmask, military drive, benedict penguin, Cotton wool
    x0 = 420
    y0 = 0
    x1 = 1150
    y1 = 1030
    haystack_img = haystack_img[y0:y1, x0:x1]



    needle_img = cv.imread(needle_img, cv.IMREAD_UNCHANGED)
    method = cv.TM_CCOEFF_NORMED
    needle_img = cv.cvtColor(needle_img, cv.COLOR_RGBA2RGB)
    # Save the dimensions of the needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    # There are 6 methods to choose from:
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED


    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
    # Get the all the positions from the match result that exceed our threshold
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    # print(locations)
    '''if np.where(result >= threshold):
        print("Klickade på detta resultatet" + str(locations))'''

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
    #print("Rektanglar" + str(rectangles))

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
            center_x = x + int(w / 2) + 420
            center_y = y
            #Här går sakerna för att droppa
            time.sleep(0.1)
            pyautogui.keyDown('ctrl')
            pyautogui.moveTo(center_x, center_y, 0.1)

            #pywinauto.mouse.move(coords=(center_x, center_y))
            pyautogui.click()
            pyautogui.keyUp('ctrl')
            '''cv.rectangle(haystack_img, (x, y), (x+needle_w, y+needle_h), (0, 255, 0), 5)
            cv.imshow("asd", haystack_img)
            cv.waitKey(10000)'''
            # Save the points
            points.append((center_x, center_y))

            # Determine the box position
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # Draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, color=line_color,
                         lineType=line_type, thickness=2)

