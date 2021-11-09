import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

#Import custom modules
from dataSystem import timeplan
import colors
class AddEventWindow:
    def __init__(self, rootWin, cCal, font):
        #Self variables
        self.root = tk.Toplevel(rootWin)
        self.root.configure(bg = colors.background)

        #Styling
        self.style = ttk.Style(rootWin)
        self.style.theme_use('clam')
        timeArray = []
        for i in range (0, 25):
            if len(str(i)) < 2:
                i = f'0{i}'
            timeArray.append(f'{i}:00')
        #Calendar
        self.cCal = cCal
        
        #Variables
        self.startTime = tk.StringVar(value=timeArray[0])
        self.endTime = tk.StringVar(value=timeArray[0])
        self.date = tk.StringVar()
        
        #Labels
        self.dateL = ttk.Label(self.root, text='Date')
        self.nameL = ttk.Label(self.root, text='Event Name')
        self.startL = ttk.Label(self.root, text='Start time')
        self.endL = ttk.Label(self.root, text='End time')
        self.descL = ttk.Label(self.root, text='description')

        #Actual shit
        self.dateE = DateEntry(self.root, state='NORMAL', style='TEntry')
        self.nameE = ttk.Entry(self.root, style='TEntry')
        self.startE = ttk.OptionMenu(self.root, self.startTime, *timeArray,
                                     style='TMenubutton')
        self.endE = ttk.OptionMenu(self.root, self.endTime, *timeArray)
        self.descE = tk.Text(self.root, **colors.tkTextColors,
                             width = 50, height=5)
        self.addButton = ttk.Button(self.root, text='Add Event',
                                    command=self.addEvent, style='c.TButton')

        #Configure the grid
        tk.Grid.columnconfigure(self.root, 0, weight=1, minsize=40)
        tk.Grid.columnconfigure(self.root, 1, weight=1)

        tk.Grid.rowconfigure(self.root, 0, weight=0)
        tk.Grid.rowconfigure(self.root, 1, weight=0)
        tk.Grid.rowconfigure(self.root, 2, weight=0)
        tk.Grid.rowconfigure(self.root, 3, weight=0)
        tk.Grid.rowconfigure(self.root, 4, weight=0)
        tk.Grid.rowconfigure(self.root, 5, weight=0)

        #Labels in grid
        self.dateL.grid(column=0, row=0, sticky='ns')
        self.nameL.grid(column=0, row=1, sticky='ns')
        self.startL.grid(column=0, row=2, sticky='ns')
        self.endL.grid(column=0, row=3, sticky='ns')
        self.descL.grid(column=0, row=4, sticky='n')

        #Entrys in grid
        self.dateE.grid(column=1, row=0, sticky='nsew')
        self.nameE.grid(column=1, row=1, sticky='nsew')
        self.startE.grid(column=1, row=2, sticky='w')
        self.endE.grid(column=1, row=3, sticky='w')
        self.descE.grid(column=1, row=4, sticky='nsew')

        #Button in grid
        self.addButton.grid(column=0, row=5, sticky='e')

    def addEvent(self):
        date = self.dateE.get_date()
        dateStr = datetime.strftime(date, '%-m/%-d/%y')
        print(dateStr)
        name = self.nameE.get()
        startTime = self.startTime.get()
        endTime = self.endTime.get()
        desc = self.descE.get('1.0', 'end')
        timeplan.set(dateStr, name, startTime, endTime, desc)
        calendarModule = self.cCal
        calendarModule.addEvent(date, name, desc)
        print("Added event")
        self.root.destroy()
