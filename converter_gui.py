
import PySimpleGUI as sg

operations = {
    "km to mile": lambda i: ("kilometres", i * 0.6214, "miles"),
    "mile to km": lambda i: ("miles", i / 0.6214, "kilometres"),
    "kg to pound": lambda k: ("kilograms", k * 2.20462, "pounds"),
    "pound to kg": lambda l: ("pounds", l / 2.20462, "kilograms")    
}

layout = [
    [
        sg.Input(key="-ENTRY-"),
        sg.Spin(list(operations.keys()), key="-OPERATION-"),
        sg.Button("Convert", key="-CONVERT-")
    ],
    [sg.Text("Output", key="-OUTPUT-")]
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "-CONVERT-":
        try:
            user_entry = float(values["-ENTRY-"])
        except:
            window["-OUTPUT-"].update("Please enter a number.")
            continue
        
        result = operations[values["-OPERATION-"]](user_entry)
        window["-OUTPUT-"].update(f"{user_entry} {result[0]} are {result[1]:.3f} {result[2]}")

window.close()
