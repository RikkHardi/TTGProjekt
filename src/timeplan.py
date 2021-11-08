#import modules
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import tkinter.font as tkFont

#import custom modules
from dataSystem import timeplan as tp
class Timeplan:
    def __init__(self, rootWin):
        #Self variables
        self.background = '#191A19'
        self.foreground = '#D8E9A8'
        self.labelBackground = 'black'
        self.rootWindow = rootWin
        self.wFrame = tk.Frame(rootWin, borderwidth=2, relief='groove',
                          height=240, background=self.background)
        self.displayedEvents = []
        self.font = None

        #Create the grid
        tk.Grid.columnconfigure(self.wFrame, 0, weight=1)
        for i in range(0, 25):
            tk.Grid.rowconfigure(self.wFrame, i, weight=1, minsize=3)

    def updateTimetable(self, selectedDay):
        for widget in self.displayedEvents:
            widget.grid_forget()
        try:
            print(selectedDay)
            events = tp.get()[selectedDay]
        except KeyError:
            print(KeyError)
            return
        eventsNames = events.keys()

        for event in eventsNames:
            startTime = events[event][0]
            endTime = events[event][1]
            startGrid = int(startTime[:2])
            endGrid = int(endTime[:2])
            span = endGrid - startGrid
            desc = events[event][2]
            l = ttk.Label(self.wFrame, font=self.font, text=f'{event}\n{startTime}-{endTime}\n{desc}',
                          background=self.labelBackground, foreground=self.foreground)
            l.grid(row=startGrid, rowspan=span, sticky='nsew')
            self.displayedEvents.append(l)
            
        
        
            
        
