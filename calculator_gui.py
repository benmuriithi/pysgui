

#Simple Calculator App
#Requires PySimpleGUI and tkinter

import PySimpleGUI as sg

theme_menu = ["menu", ["LightBlue2", "DarkBlack", "LightGrey", "random"]]
operations = {i for i in "/X-+"}

def create_window(theme: str) ->sg.Window:
    sg.theme(theme)
    sg.set_options(font = "franklin 14", button_element_size=(5,2))
    normal_button_size = (5,2)
    layout = [
        [
            sg.Text(
                text='', key="SCREEN", font="franklin 20", expand_x=True,
                justification='right', pad=(4,17), right_click_menu=theme_menu
            )
        ],
        [
            sg.Button(button_text="E", key="ENTER", expand_x=True),
            sg.Button(button_text="C", key='CLEAR', expand_x=True)
        ],
        [
            sg.Button(button_text=i, key=f'{i}', size=normal_button_size) for i in "789/"
        ],
        [
            sg.Button(button_text=i, key=f'{i}', size=normal_button_size) for i in "456X"
        ],
        [
            sg.Button(button_text=i, key=f'{i}', size=normal_button_size) for i in "123-"
        ],
        [
            sg.Button(button_text="0", key="0", expand_x=True, expand_y=True),
            sg.Button(button_text=".", key='.', size=normal_button_size),
            sg.Button(button_text="+", key='+', size=normal_button_size),
        ]
    ]

    return sg.Window("Calculator", layout, icon="./resources/calculator.ico")

number_buttons = {str(i) for i in range(10)}
number_buttons.add('.')

window = create_window("LightBlue2")
answer_displayed_flag = False
math_error = False

clear_screen = lambda: window["SCREEN"].update('')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event in theme_menu[1]:
        window.close()
        window = create_window(event)
    elif event in number_buttons:
        if answer_displayed_flag or math_error:
            clear_screen()
            math_error = False
        window["SCREEN"].update(window["SCREEN"].get()+event)
        answer_displayed_flag = False
    elif event in operations:
        if math_error:
            clear_screen()
            math_error = False
        if event == "X":
            event = "*"
        window["SCREEN"].update(window["SCREEN"].get()+event)
        answer_displayed_flag = False
    elif event == "ENTER":
        if math_error:
            clear_screen()
            math_error = False
        try:
            window["SCREEN"].update(round(eval(window["SCREEN"].get()), 12))
        except:
            window["SCREEN"].update("MATH ERROR")
            math_error=True
        else:
            answer_displayed_flag = True
    elif event == "CLEAR":
        clear_screen()

window.close()