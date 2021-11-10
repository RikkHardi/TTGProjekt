#dt colors
background = '#101010'
surface = '#2E2E2E'
primary = '#7ABB00'
secondary = '#9CB4D5'
cancel = '#ff542e'
onBackground = '#FFFFFF'
onSurface = '#FFFFFF'
onPrimary = '#FFFFFF'
onSecondary = '#1E1E1E'

#Color kwargs

#Basic colors
basicColoring = {'background' : surface, 'foreground' : onSurface, 'bordercolor' : background, 'relief' : 'flat'}
basicColoringBorders = {'background' : surface, 'foreground' : onSurface,
                        'bordercolor' : background, 'relief' : 'solid', 'borderwidth' : 2}

#Calendar colors
calendarColors = {'background' : background, 'disabledbackground' : background, 'normalbackground' : surface,
                  'bordercolor' : background,
                  'foreground' : onSurface, 'normalforeground' : onSurface,
                  'headersbackground' : background, 'headersforeground' : onBackground,
                  'weekendbackground' : primary, 'weekendforeground' : onPrimary,
                  'othermonthbackground' : background, 'othermonthforeground' : surface,
                  'othermonthwebackground' : surface,
                  'selectbackground' : secondary, 'selectforeground' : onSecondary,
                  'tooltipbackground' : primary, 'tooltipforeground' : onPrimary}

#tk.Frame coloring properties
tkFrameColors = {'relief' : 'flat', 'borderwidth' : 0, 'background' : background}

#tk.Text coloring properties
tkTextColors = {'background' : surface, 'foreground' : onSurface,
                'highlightthickness' : 0,
                'insertbackground' : 'white',
                'bd' : 1}

#ttk.Entry and tkcalendar.DataEntry coloring properties
entryColors = {'background' : surface, 'foreground' : onSurface, 'fieldbackground' : surface,
               'bd' : 0,
               'highlightcolor' : background,
               'relief' : 'flat',
               'selectborderwidth' : 0,
               'insertcolor' : onSurface}

#ttk.OptionMenu coloring properties
menubuttonColors = {'background' : [('!active', surface), ('active', primary)],
               'foreground' : [('!active',onSurface), ('active', onPrimary)],
               'fieldbackground' : [('!active', surface), ('active', primary)],
                    'relief' : 'flat'}

ttkLabelColors = {'background' : secondary, 'foreground' : onSecondary,
                  'relief' : 'flat'}

ttkHoverColors = {'background' : [('!active', surface), ('active', primary)]
                  , 'foreground' : [('!active', onSurface), ('active', onPrimary)],
                  'relief' : 'flat'}

#ttk.Button coloring properties
ttkButtonColors = {'background' : [('!active', surface), ('active', primary)]
                  , 'foreground' : [('!active', onSurface), ('active', onPrimary)],
                  'relief' : 'flat'}

ttkCancelColors = {'background' : [('!active', surface), ('active', cancel)]
                  , 'foreground' : [('!active', onSurface), ('active', onSecondary)],
                  'relief' : 'flat'}

