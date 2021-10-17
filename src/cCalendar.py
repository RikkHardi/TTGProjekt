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
        self.font = tkFont.Font(family='Futura', size=10)

        #Init code
        bgcolor = '#191A19'   #background
        fgcolor = '#D8E9A8'   #text
        bgwknd = '#1E5128'   #weekendBackground
        fghidden = bgwknd #next month text 
        bgwkhid = '#D8E9A8'  #next month weekend

        #Create calendar widget
        self.cal = Calendar(rootWin, font=self.font,
                            height=400, width=500,
                       background = bgcolor, disabledbackground = bgcolor, normalbackground = bgcolor,
                       bordercolor = bgcolor,
                       foreground = fgcolor, normalforeground = fgcolor,
                       headersbackground = bgcolor, headersforeground = fgcolor,
                       weekendbackground = bgwknd, weekendforeground = fgcolor,
                       othermonthbackground = bgcolor, othermonthforeground = fghidden,
                       othermonthwebackground = bgwkhid,
                       year=self.today.year,
                       month=self.today.month,
                       day=self.today.day)

        #Binds callback to dateclick event
        self.cal.bind("<<CalendarSelected>>", self.CalendarSelectedCallback)

        #Debug (creates events into the calendar)
        timeplan.set('10/9/21', 'Event', '18:00', '19:00')
        timeplan.set('10/11/21', 'Event2', '17:00', '19:00')
        timeplan.set('10/11/21', 'Event3', '12:00', '16:00')
        timeplan.set('10/11/21', 'Event4', '16:00', '17:00')
        timeplan.set('10/11/21', 'Event5', '19:00', '20:00')
        timeplan.set('10/11/21', 'Event6', '09:00', '10:00')

        #Adds saved events to the calendar
        eventsDict = timeplan.get()
        for dateR in eventsDict.keys():
            for event in eventsDict[dateR].keys():
                self.addEvent(datetime.strptime(dateR, '%m/%d/%y'), event, eventsDict[dateR][event][2])
        
    def CalendarSelectedCallback(self, event):
        self.timetable.updateTimetable(self.cal.get_date())

    def addEvent(self, dateA, event, desc):
        self.cal.calevent_create(dateA, event, desc)



