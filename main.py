import threading
from window import window

#might use later
#import pyautogui

windowThread = threading.Thread(target=window)
windowThread.start()
