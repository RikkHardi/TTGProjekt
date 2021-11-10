import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

#Import custom modules
from cCalendar import cCalendar
from timeplan import Timeplan
#from notesModule import notesMod
from addEventWindow import AddEventWindow

#import colors
import colors

def openAddEvent():
    w = AddEventWindow(root, cal, font)
    
root = tk.Tk()
root.title('Time Manager')
#root.geometry('310x500')
#root.resizable(0,0)

style = ttk.Style()
style.theme_use('clam')

#Configure grid
root.rowconfigure(0, weight=0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.rowconfigure(1, weight=1)
#tk.Grid.columnconfigure(root, 1, weight=0)

root.rowconfigure(2, weight=0)

#Add canvas to scroll timeplan
cv = tk.Canvas(root)
sb = ttk.Scrollbar(root, command=cv.yview)
cv['yscrollcommand'] = sb.set

#Add timeplan
tp = Timeplan(root)

#Add calendar
cal = cCalendar(root, tp)
#New event button
newEventButton = ttk.Button(root, text='New Event', command=openAddEvent,
                            style='b.TButton')

#Add notes
#notes = notesMod(root)
#Notes save button
#notesSaveButton = ttk.Button(root, text='Save',command=notes.SaveText)

#Font
font = tkFont.Font(family='Gadget', size=12)

#Configure Calendar
cal.font = font
cal.cal.configure(**colors.calendarColors)

#Configure notes
#notes.font = font
#notes.textField.configure(colors.tkTextColors)

#Configure style
style.layout(
        'c.TButton',[
            ('Button.button', None),
            ('Button.focus', {'children': [                
                ('Button.padding', {'children': [
                    ('Button.label', {'side' : 'left'}
                     )]}
                 )]}
             )]
        )
style.layout('TEntry', [
    ('Entry.highlight', {
        'sticky': 'nswe',
        'children':
            [('Entry.border', {
                'border': '1',
                'sticky': 'nswe',
                'children':
                    [('Entry.padding', {
                        'sticky': 'nswe',
                        'children':
                            [('Entry.textarea',
                              {'sticky': 'nswe'})]
                    })]
            })]
    })])

style.configure('c.TButton', anchor = 'center')
style.map('c.TButton', **colors.ttkButtonColors)
style.map('b.TButton', **colors.ttkButtonColors)
style.map('canc.TButton', **colors.ttkCancelColors)
style.configure('c.TButton.label', justify='left', side='left')
style.configure('TLabel', **colors.basicColoring)
style.configure('b.TLabel', **colors.ttkLabelColors)
style.configure('c.TLabel', **colors.basicColoringBorders)
style.configure('TEntry', **colors.entryColors)
style.map('TMenubutton', **colors.menubuttonColors)
style.configure('TFrame', **colors.tkFrameColors)



#Add to grid
cal.cal.grid(row=0, column=0, columnspan=2, sticky='nsew')
tp.wFrame.grid(row=1, column=0, columnspan=2, sticky='nsew')
#notes.wFrame.grid(row=0, column=0, rowspan=2, sticky='NSEW')
#notesSaveButton.grid(row=2, column=0, sticky='nsew')
newEventButton.grid(row=2, column=0, columnspan=2, sticky = 'nsew')

root.mainloop()
