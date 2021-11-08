import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

#Import custom modules
from cCalendar import cCalendar
from timeplan import Timeplan
from notesModule import notesMod
from addEventWindow import AddEventWindow

def openAddEvent():
    colorkw = {'background' : primaryBG, 'foreground' : primaryFG}
    w = AddEventWindow(root, cal, colorkw, font)
    
root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')

#Configure grid
tk.Grid.rowconfigure(root, 0, weight=0)
tk.Grid.columnconfigure(root, 0, weight=1)

tk.Grid.rowconfigure(root, 1, weight=1)
tk.Grid.columnconfigure(root, 1, weight=0)

tk.Grid.rowconfigure(root, 2, weight=1)

#Add timeplan
tp = Timeplan(root)

#Add calendar
cal = cCalendar(root, tp)
#New event button
newEventButton = ttk.Button(root, text='New Event', command=openAddEvent)

#Add notes
notes = notesMod(root)
#Notes save button
notesSaveButton = ttk.Button(root, text='Save',command=notes.SaveText)

#Font
font = tkFont.Font(family='Futura', size=12)

#Primary colors
primaryBG = '#191A19'
primaryFG = '#D8E9A8'

#Secondary colors
secondaryBG = '#1E5128'
secondaryFG = secondaryBG

#Tertiary colors
tertiaryBG = '#D8E9A8'

#Configure Calendar
cal.font = font
cal.cal.configure(background = primaryBG, disabledbackground = primaryBG, normalbackground = primaryBG,
                       bordercolor = primaryBG,
                       foreground = primaryFG, normalforeground = primaryFG,
                       headersbackground = primaryBG, headersforeground = primaryFG,
                       weekendbackground = secondaryBG, weekendforeground = primaryFG,
                       othermonthbackground = primaryBG, othermonthforeground = secondaryFG,
                       othermonthwebackground = tertiaryBG)

#Configure timeplan colors
tp.background = primaryBG
tp.foreground = primaryFG
tp.labelBackground = secondaryBG
tp.font = font

#Configure notes
notes.font = font
notes.textField.configure(bg = primaryBG, fg = primaryFG)

#Configure main window
style.configure('TButton', background=primaryBG, foreground=primaryFG)


#Add to grid
cal.cal.grid(row=0, column=1, sticky='NSEW')
tp.wFrame.grid(row=1, column=1, sticky='NSEW')
notes.wFrame.grid(row=0, column=0, rowspan=2, sticky='NSEW')
notesSaveButton.grid(row=2, column=0, sticky='nsew')
newEventButton.grid(row=2, column=1, sticky = 'nsew')

root.mainloop()
