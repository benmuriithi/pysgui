
import PySimpleGUI as sg
from time import time

sg.theme("LightBlue2")

def create_window():    
    layout = [
        [sg.VPush()],
        [sg.Text("00.0", font="Young 40", key="-SCREEN-")],
        [
            sg.Button("Start", key = "-STARTSTOP-", button_color=("#000000", "#0235F2"), font="young 15"),
            sg.Button("Lap", key="-LAP-", button_color=("#000000", "#0235F2"), font="young 15", visible=False)
        ],
        [sg.Column(layout = [[]], key="-LAPLIST-")],
        [sg.VPush()],
    ]

    return sg.Window(
        "Stopwatch", layout, size=(300, 300), element_justification="center",
        icon="./resources/stopwatch.ico", resizable=True,
        )

window = create_window()

start_time = 0
elapsed_time = 0
timer_active = False
num_laps = 0

while True:
    event, values = window.read(timeout=0.5)

    if event == sg.WIN_CLOSED:
        break

    if event == "-STARTSTOP-":
        if not timer_active:
            if start_time > 0:
                start_time = 0
                num_laps = 0
                window.close()
                window = create_window()
            else:
                start_time = time()
                timer_active = True
                window["-STARTSTOP-"].update("Stop")
                window["-LAP-"].update(visible=True)
        else:
            timer_active = False
            window["-STARTSTOP-"].update("Reset")
            window["-LAP-"].update(visible=False)
    
    if timer_active:
        elapsed_time = round(time() - start_time, 1)
        window["-SCREEN-"].update(elapsed_time)
    
    if event == "-LAP-":
        num_laps = num_laps + 1
        window.extend_layout(
            window["-LAPLIST-"],
            [[sg.Text(num_laps), sg.VSeparator(), sg.Text(elapsed_time)]])
    


window.close()