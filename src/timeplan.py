#import modules
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import tkinter.font as tkFont

#import custom modules
from dataSystem import timeplan as tp
import colors
from cCalendar import cCalendar
class Timeplan:
    def __init__(self, rootWin):
        #Self variables
        self.background = colors.background
        self.rootWindow = rootWin
        self.wFrame = ttk.Frame(rootWin, borderwidth=0, relief='flat',
                          height=240)
        self.displayedEvents = []
        self.font = None

    def addCal(self, cCal):
        self.cal = cCal

    def updateTimetable(self, selectedDay):
        #Delete current widgets
        for widget in self.displayedEvents:
            widget.grid_forget()

        #Check if any events today
        try:
            #print(selectedDay)
            events = tp.get()[selectedDay]
        except KeyError:
            #print(KeyError)
            return

        #Get event names and create dict by starttime
        eventsNames = events.keys()
        eventStartDict = {}
        
        for event in eventsNames:
            #get event start time
            startTime = events[event][0]

            #Convert into seconds
            delta = timedelta(hours=int(startTime[0:2]), minutes=int(startTime[3:]))
            secondsTime = delta.total_seconds()
            
            #Check if time is already in dict
            while secondsTime in eventStartDict.keys():
                secondsTime += 1

            #Add event corresponding to time in seconds to a dict
            eventStartDict[secondsTime] = event
            
        #Sort events based on their start time        
        queue = list(eventStartDict.keys())
        queue.sort()
        curRow = 0

        #Configure the column
        tk.Grid.columnconfigure(self.wFrame, 0, weight=1)
        for seconds in queue:
            #Configure new row to grid
            tk.Grid.rowconfigure(self.wFrame, curRow, weight=0)

            #Recover the event name and details
            eventName = eventStartDict[seconds]
            startTime = events[eventName][0]
            endTime = events[eventName][1]
            desc = events[eventName][2]

            #Create label and bind it to button click
            l = ttk.Button(self.wFrame, text=f'{startTime}-{endTime}\n{eventName}', style = 'c.TButton',
                           command=lambda eName=eventName, sDay=selectedDay : self.openWindow(eName, sDay))
            #l.tags(eventName)
            #l.bind('<Button-1>', lambda: self.openWindow(eventName, selectedDay))

            #Label to grid
            l.grid(row=curRow, column=0, sticky='ew', pady = 1)

            #Add to displayedEvents array
            self.displayedEvents.append(l)

            #Go to next row
            curRow += 1
    def openWindow(self, eventName, selectedDay):
        #print(self, eventName, selectedDay)
        newWin = tk.Toplevel(self.rootWindow, background=colors.background)
        newWin.geometry('200x120')
        newWin.title(eventName)
        
        events = tp.get()[selectedDay]
        startTime = events[eventName][0]
        endTime = events[eventName][1]
        desc = events[eventName][2]
        
        l = ttk.Label(newWin, text=f'{startTime}-{endTime}\n{eventName}\n\n{desc}',
                      background=colors.background)
        newWin.rowconfigure(0, weight=1)
        newWin.columnconfigure(0, weight=1)
        newWin.columnconfigure(1, weight=1)
        newWin.rowconfigure(1, weight=1)

        l.grid(row=0, column=0, columnspan=2, sticky='nw')

        deleteButton = ttk.Button(newWin, text='Delete event',
                                  command=lambda win=newWin, eName=eventName, sDay=selectedDay : self.deleteEvent(win, eName, sDay),
                                  style='canc.TButton')
        closeButton = ttk.Button(newWin, text='Close',
                                 command=newWin.destroy,
                                 style='canc.TButton')

        deleteButton.grid(row=1, column=0, sticky='nsew')
        closeButton.grid(row=1, column=1, sticky='nsew')
    def deleteEvent(self, win, name, day):
        tp.delete(name, day)
        self.updateTimetable(day)
        self.cal.delEvent(datetime.strptime(day, '%d.%m.%y'), name)
        win.destroy()
        
            
        
        
            
        
