import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time
from pystray import Icon, MenuItem as item, Menu
from PIL import Image, ImageDraw

# === Global for prompt input field coordinates ===
PROMPT_POSITION = [4348, 1183]

# === All prompts ===
ALL_PROMPTS = [
    "Continue", "Proceed", "Read all the files and report what’s happening",
    "Fix the errors", "Test the program", "Regenerate the last response",
    "Improve this code and explain changes", "Refactor for modularity",
    "Review all code files", "Build a dashboard", "Add logging",
    "Explain step by step", "Turn into Python script", "Write a README",
    "Create an API using FastAPI"
]

recent_prompts = []

# === Core functions ===

def send_prompt(text):
    def do_type():
        pyautogui.click(PROMPT_POSITION[0], PROMPT_POSITION[1])
        time.sleep(0.2)
        pyautogui.write(text, interval=0.01)
        pyautogui.press('enter')
    threading.Thread(target=do_type).start()

def update_prompt_history(prompt):
    if prompt in recent_prompts:
        recent_prompts.remove(prompt)
    recent_prompts.insert(0, prompt)
    if len(recent_prompts) > 3:
        recent_prompts.pop()
    update_recent_buttons()

def update_recent_buttons():
    for i in range(3):
        if i < len(recent_prompts):
            btn_text = recent_prompts[i]
            recent_buttons[i].config(text=btn_text, state=tk.NORMAL)
        else:
            recent_buttons[i].config(text="(empty)", state=tk.DISABLED)

def on_recent_click(index):
    text = recent_buttons[index]['text']
    if text and text != "(empty)":
        update_prompt_history(text)
        send_prompt(text)
        preview_var.set(f"Sent: {text}")

def on_run_dropdown():
    text = prompt_var.get()
    if text:
        update_prompt_history(text)
        send_prompt(text)
        preview_var.set(f"Sent: {text}")

def set_cursor_position():
    preview_var.set("🖱️ You have 3 seconds to left-click at the prompt location...")

    def wait_and_capture():
        time.sleep(3)
        x, y = pyautogui.position()
        PROMPT_POSITION[0], PROMPT_POSITION[1] = x, y
        pos_label.config(text=f"🧭 Prompt Pos: ({x}, {y})")
        preview_var.set(f"✅ Position set to ({x}, {y})")

    threading.Thread(target=wait_and_capture).start()

# === System Tray ===
def create_tray_icon():
    image = Image.new('RGB', (64, 64), color='black')
    d = ImageDraw.Draw(image)
    d.rectangle((16, 16, 48, 48), fill='white')

    def on_quit(icon, item):
        icon.stop()
        root.quit()

    icon = Icon("LazyPrompter", image, "Lazy Prompter", menu=Menu(
        item('Quit', on_quit)
    ))
    threading.Thread(target=icon.run, daemon=True).start()

# === GUI Setup ===
root = tk.Tk()
root.title("🧠 Lazy Prompter")
root.geometry("450x420")
root.resizable(False, False)
root.attributes('-topmost', True)

# Style
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 10), padding=5)
style.configure("TCombobox", padding=5)
style.configure("TLabel", font=("Segoe UI", 9), background="#1e1e1e", foreground="#ffffff")
style.configure("TFrame", background="#1e1e1e")

frame = ttk.Frame(root, padding=12)
frame.pack(fill=tk.BOTH, expand=True)

# Recent Prompts
ttk.Label(frame, text="🕘 Recent Prompts:").pack(anchor="w", pady=(0, 5))
recent_buttons = []
for i in range(3):
    btn = ttk.Button(frame, text="(empty)", width=52, command=lambda i=i: on_recent_click(i))
    btn.pack(pady=2)
    recent_buttons.append(btn)

# Dropdown + Run
ttk.Label(frame, text="📋 Choose a Prompt:").pack(anchor="w", pady=(10, 3))
prompt_var = tk.StringVar()
dropdown = ttk.Combobox(frame, textvariable=prompt_var, values=ALL_PROMPTS, width=49)
dropdown.pack()

run_button = ttk.Button(frame, text="🚀 Run Selected Prompt", command=on_run_dropdown)
run_button.pack(pady=10)

# Prompt position section
ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=10)
ttk.Label(frame, text="🖱️ Prompt Input Position:").pack(anchor="w", pady=(5, 3))
pos_label = ttk.Label(frame, text=f"🧭 Prompt Pos: ({PROMPT_POSITION[0]}, {PROMPT_POSITION[1]})")
pos_label.pack()
pos_btn = ttk.Button(frame, text="🎯 Set Prompt Position", command=set_cursor_position)
pos_btn.pack(pady=6)

# Preview
preview_var = tk.StringVar(value="No prompt sent yet.")
preview_label = ttk.Label(frame, textvariable=preview_var, foreground="lightgreen")
preview_label.pack(pady=8)

# Load default recent prompts
for default in ["Fix the errors", "Test the program", "Proceed"]:
    update_prompt_history(default)

# Launch tray icon
create_tray_icon()

# Run app
root.mainloop()
