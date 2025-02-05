import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

window = sg.Window('My To-Do App', layout=[[label],[input_box, add_button], [edit_button, complete_button],[exit_button]]) # Window Title
window.read()
window.close()


