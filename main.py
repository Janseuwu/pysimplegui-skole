import PySimpleGUI as sg
from win32api import GetSystemMetrics
import os.path
from tkinter import filedialog
import keyboard
import time

def save_file():
    dir = filedialog.askdirectory() # asks user to pick a directory


# launches a window with a text editor
def txt_editor():
    f = open('.txt', 'w')
    menu_def = [
        ['File',['New','Open','Save','Save As','---','Exit']],
        ['Edit',['Undo','---','Cut','Copy','Paste','Delete','---','Find...','Replace...','---','Select All']],
        ]

    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    layout = [
        [sg.Text('Name of file', key='-NAMETEXT-'), sg.InputText(size=(180), key='-FILENAME-'), sg.Save("Save")],
        [sg.Menu(menu_definition=menu_def)],
        [sg.Multiline(size=(width, height), key='-BODY-')],
    ]
    title = 'Text file'

    # create our text editor window
    window = sg.Window(title, layout, resizable=True, grab_anywhere_using_control=True).Finalize()
    window.Maximize()

    while True:

        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'New':
            print(values['-BODY-'])
        if event == 'Open':
            dir = filedialog.askopenfilename()
            f = open(dir, 'r')
            content = f.read()
            f.close()

            body = window['-BODY-']
            body.update(body.get() + content)            
            

        if event == 'Save':
            if '.' in values['-FILENAME-']:
                dir = filedialog.askdirectory()
                name = values['-FILENAME-']
                completeName = os.path.join(dir, name)
                f = open(completeName, 'w')
                f.write(values['-BODY-'])
                f.close()
            elif values['-FILENAME-'] == '':
                window['-NAMETEXT-'].update('Give the file a name', text_color='red')
            else:
                window['-NAMETEXT-'].update('Give file an extension', text_color='red')
        if event == 'Save As':
            if '.' in values['-FILENAME-']:
                dir = filedialog.askdirectory()
                name = values['-FILENAME-']
                completeName = os.path.join(dir, name)
                f = open(completeName, 'w')
                f.write(values['-BODY-'])
                f.close()
            elif values['-FILENAME-'] == '':
                window['-NAMETEXT-'].update('Give the file a name', text_color='red')
            else:
                window['-NAMETEXT-'].update('Give file an extension', text_color='red')
        if event == 'Exit':
            window.close()
        
def login():            
    if values[0] == password: 
        window.close()
        txt_editor() # calls function that opens the text editor
    elif values[0] != password:
        if values[0] == '':
            window['-TEXT-'].update('Field is empty')
        else:
            window['-TEXT-'].update('Wrong password')       

password = 'gaide gad' # ideally we should use dotenv with some hashing
title = 'Login'
layout = [
    [sg.Text('Insert password', key='-TEXT-')],
    [sg.InputText(password_char='*')],
    [sg.Button('Cancel'), sg.Sizer(207), sg.Button('Submit', bind_return_key=True)]
]

# create our password window
window = sg.Window(title, layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    # checks if password matches the set password
    if event == 'Submit':
        login()


# TODO        
# save funktion, bare faa knapperne til at virke egentlig