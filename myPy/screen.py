import pyautogui


def screenimg():
    try:
        pyautogui.screenshot(r'C:\Min\screen.jpg')
    except:
        pass