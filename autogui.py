import pyautogui

def booya():
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()

    pyautogui.moveTo(700, 635)
    pyautogui.click()
