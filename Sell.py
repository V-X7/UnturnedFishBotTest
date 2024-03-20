import time
import pywinauto
import pyautogui
import keyboard as k


def sälja():
    pyautogui.click()
    time.sleep(3.5)
    lista = [172, 243, 359, 467, 579, 682, 790, 908, 993]
    pyautogui.press("e")
    time.sleep(0.2)
    pyautogui.press("f")
    time.sleep(0.2)
    pyautogui.press("f")
    time.sleep(0.2)

    pywinauto.mouse.move(coords=(911, 820))
    pyautogui.click()
    pywinauto.mouse.move(coords=(366, 0))
    pyautogui.keyDown("ctrl")



    for x in range(9):
        time.sleep(0.2)
        pywinauto.mouse.move(coords=(366, lista[x]))
        pyautogui.click()


        print(lista[x])
    pyautogui.keyUp("ctrl")
    pyautogui.press("esc")
    time.sleep(0.4)
    pyautogui.press("esc")
    pyautogui.press("e")
    pyautogui.mouseDown()
    time.sleep(1.9)
    pyautogui.mouseUp()






