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
        self.padding = 2
        
        #Labels
        self.dateL = ttk.Label(self.root, text='Date')
        self.nameL = ttk.Label(self.root, text='Event Name')
        self.startL = ttk.Label(self.root, text='Start time')
        self.endL = ttk.Label(self.root, text='End time')
        self.descL = ttk.Label(self.root, text='description')

        #Actual shit
        self.dateE = DateEntry(self.root, state='NORMAL', style='TEntry', date_pattern='dd-mm-yyyy')
        self.dateE.set_date(cCal.cal.get_date())
        self.nameE = ttk.Entry(self.root, style='TEntry')
        self.startE = ttk.OptionMenu(self.root, self.startTime, *timeArray,
                                     style='TMenubutton')
        self.endE = ttk.OptionMenu(self.root, self.endTime, *timeArray)
        self.descE = tk.Text(self.root, **colors.tkTextColors,
                             width = 50, height=5)
        self.addButton = ttk.Button(self.root, text='Add Event',
                                    command=self.addEvent, style='b.TButton')
        self.cancelButton = ttk.Button(self.root, text='Cancel',
                                       command=self.root.destroy, style='canc.TButton')

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
        self.dateL.grid(column=0, row=0, sticky='nsew', pady=self.padding)
        self.nameL.grid(column=0, row=1, sticky='nsew', pady=self.padding)
        self.startL.grid(column=0, row=2, sticky='nsew', pady=self.padding)
        self.endL.grid(column=0, row=3, sticky='nsew', pady=self.padding)
        self.descL.grid(column=0, row=4, sticky='nsew', pady=self.padding)

        #Entrys in grid
        self.dateE.grid(column=1, row=0, sticky='nsw', pady=self.padding)
        self.nameE.grid(column=1, row=1, sticky='nsw', pady=self.padding)
        self.startE.grid(column=1, row=2, sticky='w', pady=self.padding)
        self.endE.grid(column=1, row=3, sticky='w', pady=self.padding)
        self.descE.grid(column=1, row=4, sticky='nsw', pady=self.padding)

        #Button in grid
        self.addButton.grid(column=1, row=5, sticky='ew')
        self.cancelButton.grid(column=0, row=5, sticky='ew')

    def addEvent(self):
        date = self.dateE.get_date()
        print(date)
        dateStr = datetime.strftime(date, '%d.%m.%y')
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
