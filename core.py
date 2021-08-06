import tkinter as tk
import pyautogui as clicky
import keyboard as kb
import time


class WindowInputs:

    def __init__(self):
        self.minColumnSize = 110
        self.minRowSize = 50
        self.mouseKey = "left"
        self.startKey = '*'
        self.stopKey = '-'
        self.cps = 10
        self.outputText = "Started"
        
    def window(self):
        root = tk.Tk()
        root.title("Chocobo Clicker")

        mouseKey = tk.StringVar()
        mouseKey.set(self.mouseKey)
        outputText = tk.StringVar()
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
        outputTextLabel = tk.Label(textvariable=outputText,relief=tk.GROOVE)
        outputTextLabel.grid(row=2,column=1,padx=5,pady=5)
    
        #text boxes
        clickSpeedEntry = tk.Entry(width=8)
        clickSpeedEntry.grid(row=1, column=0, padx=5, pady=5)
        startKeyEntry = tk.Entry(width=5)
        startKeyEntry.grid(row=1, column=1, padx=5, pady=5)
        stopKeyEntry = tk.Entry(width=5)
        stopKeyEntry.grid(row=1, column=2, padx=5, pady=5)
    
        #buttons
        refreshButton = tk.Button(text="Refresh inputs", relief=tk.RIDGE, borderwidth=5, command=lambda: self.refreshInputs(startKeyEntry.get(), stopKeyEntry.get(), clickSpeedEntry.get()))
        refreshButton.grid(row=2, column=0, padx=15)
        mouseKeyToggle = tk.Button(textvariable=mouseKey, command=lambda: self.toggleMouseKey(mouseKey), relief=tk.RIDGE, borderwidth=5, width=5)
        mouseKeyToggle.grid(row=2, column=2)
        while True:
            root.update()
            self.autoClick()
            startKeyEntry.delete(1, 'end')
            stopKeyEntry.delete(1, 'end')
            clickSpeedEntry.delete(8, 'end')
            outputText.set(f"Output:\n {self.outputText} ")

    def autoClick(self):
        if kb.is_pressed(self.startKey) == True:
            time.sleep(0.2)
            print("debug1")
        elif kb.is_pressed(self.stopKey) == True:
            time.sleep(0.2)
            print("debug2")

    def toggleMouseKey(self, mouseKey):
        if self.mouseKey == "left":
            self.mouseKey = "right"
            mouseKey.set(self.mouseKey)
        else:
            self.mouseKey = "left"
            mouseKey.set(self.mouseKey)

    def refreshInputs(self, startKey, stopKey, cps):
        self.startKey = startKey
        self.stopKey = stopKey
        self.cps = cps
        print(startKey,stopKey,cps)
