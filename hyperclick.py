import pyautogui

try:
    confirm = pyautogui.confirm()
    if (confirm == "OK"):
        while True:
            pyautogui.click(x=1000, y=500, interval=0.0001)
except KeyboardInterrupt:
    print("Done.")