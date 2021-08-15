from PIL.ImageOps import grayscale
import pyautogui

pic = pyautogui.locateCenterOnScreen('github.png', grayscale=True)
print(pic)
pyautogui.click(pic.x, pic.y)