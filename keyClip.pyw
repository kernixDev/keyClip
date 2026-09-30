import pyautogui
import win32clipboard
import keyboard

def upperCase():
    try:
        pyautogui.hotkey("ctrl", "c")

        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(data.upper())
        win32clipboard.CloseClipboard()

        pyautogui.hotkey("ctrl", "v")
    except Exception as f:
        print(f)
        pass

def lowerCase():
    try:
        pyautogui.hotkey("ctrl", "c")

        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(data.lower())
        win32clipboard.CloseClipboard()

        pyautogui.hotkey("ctrl", "v")
    except Exception as f:
        print(f)
        pass

def camelCase():
    try:
        pyautogui.hotkey("ctrl", "c")

        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        words = data.split()
        cameled = words[0].lower() + "".join(word.capitalize() for word in words[1:])

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(cameled)
        win32clipboard.CloseClipboard()

        pyautogui.hotkey("ctrl", "v")

    except Exception as f:
        print(f)

keyboard.add_hotkey("ctrl+F1", upperCase)
keyboard.add_hotkey("ctrl+F2", lowerCase)
keyboard.add_hotkey("ctrl+F3", camelCase)
keyboard.wait()