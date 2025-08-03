import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time

# 🧠 Your Prompt Location (Set this once)
PROMPT_X = 4348  # Replace with your own X
PROMPT_Y = 1183  # Replace with your own Y

# 📋 All available prompts
ALL_PROMPTS = [
    "Continue",
    "Proceed",
    "Read all the files and report what’s happening",
    "Fix the errors",
    "Test the program",
    "Regenerate the last response",
    "Improve this code and explain changes",
    "Refactor this for modularity and readability",
    "Make the UI cleaner and more usable",
    "Review all code files and dependencies",
    "Build a simple dashboard for this project",
    "Add basic logging to track what’s happening",
    "Explain this step by step",
    "Turn this into a Python script",
    "Write a README for this project",
    "Create a basic API using FastAPI"
]

# 📦 Stores the 3 most recently used prompts
recent_prompts = []

# 🧠 Function to type prompt text at the given location
def send_prompt(text):
    def do_type():
        pyautogui.click(PROMPT_X, PROMPT_Y)
        time.sleep(0.2)
        pyautogui.write(text, interval=0.01)
        pyautogui.press('enter')
    threading.Thread(target=do_type).start()

# 🔁 Update recent prompt buttons
def update_recent_buttons():
    for i in range(3):
        if i < len(recent_prompts):
            recent_buttons[i].config(text=recent_prompts[i], state=tk.NORMAL)
        else:
            recent_buttons[i].config(text="", state=tk.DISABLED)

# 🎯 On recent prompt click
def on_recent_click(index):
    text = recent_buttons[index]['text']
    if text:
        update_prompt_history(text)
        send_prompt(text)

# ➕ Update prompt history and reorder
def update_prompt_history(prompt):
    if prompt in recent_prompts:
        recent_prompts.remove(prompt)
    recent_prompts.insert(0, prompt)
    if len(recent_prompts) > 3:
        recent_prompts.pop()
    update_recent_buttons()

# 🔘 On dropdown run button
def on_run_dropdown():
    text = prompt_var.get()
    if text:
        update_prompt_history(text)
        send_prompt(text)

# 🪟 UI Setup
root = tk.Tk()
root.title("Lazy Prompter")
root.attributes('-topmost', True)
root.geometry("350x250")
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="🔁 Recent:").pack(anchor="w")

recent_buttons = []
for i in range(3):
    btn = tk.Button(frame, text="", width=40, command=lambda i=i: on_recent_click(i))
    btn.pack(pady=2)
    recent_buttons.append(btn)

tk.Label(frame, text="🔽 All Prompts").pack(pady=(10, 2), anchor="w")
prompt_var = tk.StringVar()
dropdown = ttk.Combobox(frame, textvariable=prompt_var, values=ALL_PROMPTS, width=45)
dropdown.pack()

run_btn = tk.Button(frame, text="Run Prompt", command=on_run_dropdown, width=40, bg="lightblue")
run_btn.pack(pady=8)

# Start with 3 default recents
for default in ["Fix the errors", "Test the program", "Proceed"]:
    update_prompt_history(default)

# Launch it!
root.mainloop()
