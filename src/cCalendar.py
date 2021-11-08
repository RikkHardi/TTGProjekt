#Import modules
try:
    import tkinter as tk
    from tkinter import ttk
    import tkinter.font as tkFont
except ImportError:
    print(f'Encountered import error, trying alternative imports...')
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry
from datetime import date, datetime

#Import custom modules
from dataSystem import timeplan

#Create calendar class        
class cCalendar:
    def __init__(self, rootWin, timetable):
        #Create self variables
        self.today = date.today()
        self.darkmode = True
        self.rootWindow = rootWin
        self.timetable = timetable
        self.font = None

        #Create calendar widget
        self.cal = Calendar(rootWin, font=self.font,
                            height=400, width=500,
                       year=self.today.year,
                       month=self.today.month,
                       day=self.today.day)

        #Binds callback to dateclick event
        self.cal.bind("<<CalendarSelected>>", self.CalendarSelectedCallback)

        #Adds saved events to the calendar
        eventsDict = timeplan.get()
        for dateR in eventsDict.keys():
            for event in eventsDict[dateR].keys():
                self.addEvent(datetime.strptime(dateR, '%m/%d/%y'), event, eventsDict[dateR][event][2])
        
    def CalendarSelectedCallback(self, event):
        self.timetable.updateTimetable(self.cal.get_date())

    def addEvent(self, dateA, event, desc):
        self.cal.calevent_create(dateA, event, desc)



