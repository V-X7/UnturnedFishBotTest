import cv2 as cv
hej = cv.imread("craft pa gold med alla.png")
hej = cv.resize(hej, (1366, 768))
cv.imwrite("craft pa gold med fast i laptop.png", hej)