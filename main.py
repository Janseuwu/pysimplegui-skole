import PySimpleGUI as sg

# launches a window with a text editor
def txt_editor():

    menu_def = [
        ['File',['New','Open','Save','Save As','---','Exit']],
        ['Edit',['Undo','---','Cut','Copy','Paste','Delete','---','Find...','Replace...','---','Select All']],
        ]

    layout = [
        [sg.Menu(menu_definition=menu_def)],
        [sg.Multiline(size=(100, 40))],
        [sg.Text("File Name"), sg.InputText(size=(70)), sg.OptionMenu(values=['.txt', '.md', 'other'], tooltip='Choose file extension'), sg.Button("Save")]
    ]
    title = 'Text file'

    # create our text editor window
    window = sg.Window(title, layout, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
password = 'gaide gad' # ideally we should use dotenv with some hashing
title = 'Login'
layout = [
    [sg.Text('Insert password')],
    [sg.InputText(password_char='*')],
    [sg.Button('Cancel'), sg.Sizer(207), sg.Button('Submit')]
]

# create our password window
window = sg.Window(title, layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    # checks if password matches the set password
    if event == 'Submit':
        if values[0] == password: 
            window.close()
            txt_editor() # calls function that opens the text editor
            
