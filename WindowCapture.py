import time

import win32gui, win32ui, win32con
from ctypes import windll
import numpy as np
from PIL import Image
import cv2 as cv
from PIL import ImageOps
def GetScreenShot():
    # 1366 x 768
    # get the window image data

    hwnd = win32gui.FindWindow(None, 'Unturned')

    # Uncomment the following line if you use a high DPI display or >100% scaling size
    # windll.user32.SetProcessDPIAware()

    # Change the line below depending on whether you want the whole window
    # or just the client area.
    # left, top, right, bot = win32gui.GetClientRect(hwnd)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = (right) - (left)
    h = (bot) - (top)

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, (w-800), (h-470))

    saveDC.SelectObject(saveBitMap)

    # Change the line below depending on whether you want the whole window
    # or just the client area.
    # result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)


    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    # bmpstr = saveDC.GetBitmapBits(True)


    img = np.frombuffer(bmpstr, dtype="uint8")
    img.shape = ((h-470), (w-800), 4)


    img = img[..., :3]
    img = np.ascontiguousarray(img)


    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    x0 = 900
    y0 = 500
    x1 = 1000
    y1 = 810
    new_img = img[y0:y1, x0:x1]



    return new_img



#@staticmethod
def listWindowsName():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))

    win32gui.EnumWindows(winEnumHandler, None)


class WindowCapture:

    w = 0
    h = 0
    hwnd = None
    def __init__(self, window_name=None):


        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception("Window not Found: {}".format(window_name))
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
