import functions
import FreeSimpleGUI as sg

from functions import get_todos

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="_Enter Todo_", key='todo')
add_button = sg.Button("Add")
exit_button = sg.Button("Exit") # non functional
edit_button = sg.Button("Edit") # non functional
complete_button = sg.Button("Complete") # non functional


window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',12))

while True:
    event, values = window.read()

    match event:
        case "Add":
           todos = functions.get_todos()
           new_todo = values['todo'] + "\n"
           todos.append(new_todo)
           functions.write_todos(todos)

        case "Edit":
            print(values)
        case "Complete":
            print(values)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()


