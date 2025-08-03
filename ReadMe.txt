Lazy Prompter
=============

Lazy Prompter is a lightweight desktop utility for AI app builders and prompt engineers who want to automate repetitive prompt inputs using a single click.

This tool shows a simple UI button on your screen. Clicking the button automatically moves your cursor to the prompt input area, types your desired command (e.g., "Continue", "Proceed", etc.), and presses Enter. It's designed to save time and effort when working with prompt-based AI tools.

----------------------------------------------------
Features
--------

- Floating GUI button that stays on top of all windows
- One-click auto typing into any input field
- List of predefined common prompt phrases (e.g., "Continue", "Fix the code", etc.)
- Memory of 3 most recently used prompts
- Cursor position can be set dynamically by clicking the target input field
- No internet or cloud-based AI logic — runs locally
- Can be packaged as a Windows .exe for easy launching

----------------------------------------------------
How to Use
----------

1. Run the application (`lazy_prompter_gui.exe`)
2. The interface will show 3 buttons and a dropdown menu
3. Click the "🎯" (Set Cursor) button
4. Move to your prompt input box in another window and click on it
5. Return to the Lazy Prompter and click any prompt button
6. It will:
   - Move the cursor to the selected location
   - Type the chosen phrase
   - Press Enter automatically

----------------------------------------------------
Requirements (if running from source)
-------------------------------------

- Python 3.10 or higher
- pyautogui
- tkinter (comes with Python by default)

To install dependencies:
> pip install pyautogui

----------------------------------------------------
How to Package into a .exe File
-------------------------------

1. Install PyInstaller:
> py -m pip install pyinstaller

2. Run the following command:
> py -m PyInstaller --onefile --windowed lazy_prompter_gui.py

3. The final executable will be available in the "dist" folder.

----------------------------------------------------
Future Plans
------------

- Add system tray support
- Allow custom prompt input
- Dark/light theme option
- Improve support for multi-monitor workflows

----------------------------------------------------
Author
------

Built by Glorious Perpose
Automating multitasking, one click at a time.
