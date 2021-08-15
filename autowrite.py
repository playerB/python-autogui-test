import pyautogui, time

try :
    time.sleep(60)
    count = 1
    while True:
        pyautogui.write('I have been AFK for ' + str(count) + ' minutes', interval=0.15)
        time.sleep(60)
        count += 1
        pyautogui.hotkey('ctrl', 'a', 'backspace')
except KeyboardInterrupt:
    print('\nDone')