import pyautogui
import win32clipboard
import keyboard

def uppercase():
    pyautogui.hotkey("ctrl", "c")

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data.upper())
    win32clipboard.CloseClipboard()

    pyautogui.hotkey("ctrl", "v")

def lowercase():
    pyautogui.hotkey("ctrl", "c")

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data.lower())
    win32clipboard.CloseClipboard()

    pyautogui.hotkey("ctrl", "v")

keyboard.add_hotkey("ctrl+h", uppercase)
keyboard.add_hotkey("ctrl+j", lowercase)

while True:
    keyboard.wait()