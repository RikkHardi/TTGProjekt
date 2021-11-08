#import modules
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

#import custom modules
from dataSystem import notes

class notesMod:
    def __init__(self, rootWin):
        #Create self variables
        self.wFrame = tk.Frame(rootWin, borderwidth=2, relief='groove', height=260)
        self.font = None
        self.textField = tk.Text(self.wFrame, font=self.font)
        self.textField.insert('1.0', notes.get())
        
        #Configure grid
        tk.Grid.rowconfigure(self.wFrame, 0, weight=1)
        tk.Grid.columnconfigure(self.wFrame, 0, weight=1)

        #Set stuff into grid
        self.textField.grid(row=0, column=0, sticky='nsew')
    #Save textfile text
    def SaveText(self):
        text = self.textField.get('1.0', 'end')
        print('Saving following string:\n' + text)
        notes.set(text)
        
        
