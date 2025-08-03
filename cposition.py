import pyautogui
import time

print("Move your cursor to the prompt box. You have 5 seconds...")
time.sleep(5)
x, y = pyautogui.position()
print(f"X: {x}, Y: {y}")
