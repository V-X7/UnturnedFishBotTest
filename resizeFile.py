import cv2 as cv
from hsvfilter import HsvFilter
import numpy as np
hsv_filter_for_gold_text = HsvFilter(0,0,119,138,8,255,0,0,0,0)
haystack_img = cv.imread('CraftBilder/silverToGold.png')

hsv = cv.cvtColor(haystack_img, cv.COLOR_BGR2HSV)

lower = np.array([hsv_filter_for_gold_text.hMin, hsv_filter_for_gold_text.sMin, hsv_filter_for_gold_text.vMin])
upper = np.array([hsv_filter_for_gold_text.hMax, hsv_filter_for_gold_text.sMax, hsv_filter_for_gold_text.vMax])
# Apply the thresholds
haystack_img = cv.inRange(hsv, lower, upper)

cv.imshow('haystack', haystack_img)
cv.waitKey(3000)