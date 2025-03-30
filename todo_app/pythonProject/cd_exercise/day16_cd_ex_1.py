import FreeSimpleGUI as Sg

label1 = Sg.Text('Enter Feet:')
input_text1 = Sg.InputText()

label2 = Sg.Text('Enter inches:')
input_text2 = Sg.InputText()

convert_button = Sg.Button('Convert')

window = Sg.Window('Converter', layout=[
    [label1, input_text1],
    [label2, input_text2],
    [convert_button]
])

window.read()
window.close()
