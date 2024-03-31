import cv2 as cv
hej = cv.imread("StoraBilder/craft pa gold med alla.png")
hej = cv.resize(hej, (1366, 768))
cv.imwrite("StoraBilder/craft pa gold med fast i laptop.png", hej)