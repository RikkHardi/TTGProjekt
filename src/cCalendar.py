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

        self.timetable.addCal(self)

        #Create calendar widget
        self.cal = Calendar(rootWin, font=self.font,
                       year=self.today.year,
                       month=self.today.month,
                       day=self.today.day,
                            date_pattern='dd.mm.yy')

        #Binds callback to dateclick event
        self.cal.bind("<<CalendarSelected>>", self.CalendarSelectedCallback)

        #Adds saved events to the calendar
        eventsDict = timeplan.get()
        for dateR in eventsDict.keys():
            for event in eventsDict[dateR].keys():
                self.addEvent(datetime.strptime(dateR, '%d.%m.%y'), event, eventsDict[dateR][event][2])
        
    def CalendarSelectedCallback(self, event):
        self.timetable.updateTimetable(self.cal.get_date())

    def addEvent(self, dateA, event, desc):
        self.cal.calevent_create(dateA, event, desc)
        self.timetable.updateTimetable(self.cal.get_date())

    def delEvent(self, dateA, event):
        dateIDs = self.cal.get_calevents(date=dateA)
        #print(dateIDs)
        for dID in dateIDs:
            ce = self.cal.calevents[dID]['text']
            #print(f'delEvent: ({ce}) {event}')
            if ce == event:
                self.cal.calevent_remove(dID)

        



