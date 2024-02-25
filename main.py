import pyautogui, time
text = ("Chto delaesh'?")
time.sleep(5)
for i in range(50):
    pyautogui.typewrite(f'{text}')
    pyautogui.press('enter')