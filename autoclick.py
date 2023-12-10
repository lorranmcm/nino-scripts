import pyautogui
import time

print(pyautogui.position())

while True:
    pyautogui.click(x=1783, y=987)
    time.sleep(0.1)
    pyautogui.click(x=565, y=1002)
    time.sleep(0.1)
