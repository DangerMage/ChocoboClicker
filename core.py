import tkinter as tk
import pyautogui as clicky


class WindowInputs:

    def __init__(self):
        self.minColumnSize = 100
        self.minRowSize = 50
        self.mouseKey = "left"
        
    def window(self):
        root = tk.Tk()
        root.title("Chocobo Clicker")

        mouseKey = tk.StringVar()
        mouseKey.set(self.mouseKey)

        for i in range(3):
            root.columnconfigure(i, weight=1, minsize=self.minColumnSize)
            root.rowconfigure(i, weight=1, minsize=self.minRowSize)
    
        #labels
        clickSpeedLabel = tk.Label(text="Click Speed:")
        clickSpeedLabel.grid(row=0, column=0, padx=5, pady=5)
        startKeyLabel = tk.Label(text="Start Key:")
        startKeyLabel.grid(row=0, column=1, padx=5, pady=5)
        stopKeyLabel = tk.Label(text="Stop Key:")
        stopKeyLabel.grid(row=0, column=2, padx=5, pady=5)
    
        #text boxes
        clickSpeedEntry = tk.Entry(width=8)
        clickSpeedEntry.grid(row=1, column=0, padx=5, pady=5)
        startKeyEntry = tk.Entry(width=5)
        startKeyEntry.grid(row=1, column=1, padx=5, pady=5)
        stopKeyEntry = tk.Entry(width=5)
        stopKeyEntry.grid(row=1, column=2, padx=5, pady=5)
    
        #buttons
        refreshButton = tk.Button(text="Refresh inputs")
        refreshButton.grid(row=2, column=0)
        mouseKeyToggle = tk.Button(textvariable=mouseKey, command=self.toggleMouseKey(mouseKey))
        mouseKeyToggle.grid(row=2, column=2)
        while True:
            root.update()
            self.autoClick()

    def autoClick(self):
        temp = 0

    def toggleMouseKey(self, mouseKey):
        if self.mouseKey == "left":
            self.mouseKey = "right"
            mouseKey.set(self.mouseKey)
            print("Debug1")
        else:
            self.mouseKey = "left"
            mouseKey.set(self.mouseKey)
            print("Debug2")
