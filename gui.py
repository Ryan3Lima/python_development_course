import functions
import FreeSimpleGUI as sg

from functions import get_todos

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="_Enter Todo_", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45,8))

edit_button = sg.Button("Edit") # non functional
complete_button = sg.Button("Complete") # non functional
exit_button = sg.Button("Exit") # non functional

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box,edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',12))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
           todos = functions.get_todos()
           new_todo = values['todo'] + "\n"
           todos.append(new_todo)
           functions.write_todos(todos)
           window['todos'].update(values=todos)

        case "Edit":
            selected_todo = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(selected_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()


