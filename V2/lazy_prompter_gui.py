import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time

# Initial dummy values (will be updated by user)
PROMPT_POSITION = [4348, 1183]

ALL_PROMPTS = [
    "Continue", "Proceed", "Read all the files and report what’s happening",
    "Fix the errors", "Test the program", "Regenerate the last response",
    "Improve this code and explain changes", "Refactor for modularity",
    "Review all code files", "Build a dashboard", "Add logging",
    "Explain step by step", "Turn into Python script", "Write a README",
    "Create an API using FastAPI"
]

recent_prompts = []

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

# Cursor position setting logic
def set_cursor_position():
    def wait_for_click():
        preview_var.set("Move your mouse to the prompt box and left-click...")
        time.sleep(1)
        while True:
            if pyautogui.mouseDown():
                x, y = pyautogui.position()
                PROMPT_POSITION[0] = x
                PROMPT_POSITION[1] = y
                pos_label.config(text=f"🧭 Prompt Pos: ({x}, {y})")
                preview_var.set("✅ Position set!")
                break
    threading.Thread(target=wait_for_click).start()

# ==== GUI Setup ====
root = tk.Tk()
root.title("🧠 Lazy Prompter")
root.geometry("430x360")
root.resizable(False, False)
root.attributes('-topmost', True)

# Style
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 10), padding=5)
style.configure("TCombobox", padding=5)
style.configure("TLabel", font=("Segoe UI", 9), background="#1e1e1e", foreground="#ffffff")
style.configure("TFrame", background="#1e1e1e")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Recent Prompts:").pack(anchor="w")

recent_buttons = []
for i in range(3):
    btn = ttk.Button(frame, text="(empty)", width=50, command=lambda i=i: on_recent_click(i))
    btn.pack(pady=3)
    recent_buttons.append(btn)

ttk.Label(frame, text="Select from All Prompts:").pack(anchor="w", pady=(10, 3))
prompt_var = tk.StringVar()
dropdown = ttk.Combobox(frame, textvariable=prompt_var, values=ALL_PROMPTS, width=48)
dropdown.pack()

run_button = ttk.Button(frame, text="🚀 Run Selected Prompt", command=on_run_dropdown)
run_button.pack(pady=10)

preview_var = tk.StringVar(value="No prompt sent yet.")
preview_label = ttk.Label(frame, textvariable=preview_var, foreground="lightgreen")
preview_label.pack(pady=5)

# Prompt Position Button
ttk.Label(frame, text="Prompt Input Location:").pack(anchor="w", pady=(10, 0))
pos_label = ttk.Label(frame, text=f"🧭 Prompt Pos: ({PROMPT_POSITION[0]}, {PROMPT_POSITION[1]})")
pos_label.pack()

pos_btn = ttk.Button(frame, text="🖱️ Set Prompt Position", command=set_cursor_position)
pos_btn.pack(pady=5)

# Initialize recents
for default in ["Fix the errors", "Test the program", "Proceed"]:
    update_prompt_history(default)

root.mainloop()
