import pyautogui

confirmClick = pyautogui.confirm("write?")
if (confirmClick == "OK"):
    pyautogui.typewrite("hello world", interval=0.25)
    pyautogui.press("enter");