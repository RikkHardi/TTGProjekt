import tkinter as tk
from tkinter import ttk

#Import custom modules
from cCalendar import cCalendar
from timeplan import Timeplan
from notesModule import notesMod

root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')

#Configure grid
tk.Grid.rowconfigure(root, 0, weight=0)
tk.Grid.columnconfigure(root, 0, weight=1)

tk.Grid.rowconfigure(root, 1, weight=1)
tk.Grid.columnconfigure(root, 1, weight=0)

#Add timeplan
tp = Timeplan(root)

#Add calendar
cal = cCalendar(root, tp)

#Add notes
notes = notesMod(root)

#Add to grid
cal.cal.grid(row=0, column=1, sticky='NSEW')
tp.wFrame.grid(row=1, column=1, sticky='NSEW')
notes.wFrame.grid(row=0, column=0, rowspan=2, sticky='NSEW')

root.mainloop()
