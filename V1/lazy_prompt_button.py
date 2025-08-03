import tkinter as tk
import pyautogui
import threading
import time

# === Your Prompt Box Location ===
PROMPT_X, PROMPT_Y = 4348, 1183  # Set this to your actual prompt input box
PROMPT_TEXT = "Continue"
# ================================

def send_prompt():
    def run():
        time.sleep(0.2)
        pyautogui.click(PROMPT_X, PROMPT_Y)
        time.sleep(0.2)
        pyautogui.typewrite(PROMPT_TEXT)
        pyautogui.press("enter")
    threading.Thread(target=run).start()

# === Position the Button Relative to Prompt Box ===
BUTTON_WIDTH, BUTTON_HEIGHT = 120, 50
OFFSET_X = -150  # Left of prompt box
OFFSET_Y = -100  # Above prompt box

BUTTON_X = PROMPT_X + OFFSET_X
BUTTON_Y = PROMPT_Y + OFFSET_Y

# Create Floating Button
root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry(f"{BUTTON_WIDTH}x{BUTTON_HEIGHT}+{BUTTON_X}+{BUTTON_Y}")

btn = tk.Button(root, text="Continue", command=send_prompt, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
btn.pack(fill="both", expand=True)

# Allow dragging
def start_move(event):
    root.x = event.x
    root.y = event.y

def on_motion(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

btn.bind("<Button-1>", start_move)
btn.bind("<B1-Motion>", on_motion)

root.mainloop()
