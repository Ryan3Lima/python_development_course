import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkTeal2")

clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="_Enter Todo_", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45,8))

edit_button = sg.Button("Edit") # non functional
complete_button = sg.Button("Complete") # non functional
exit_button = sg.Button("Exit") # non functional

window_layout = [[clock],
                 [label],
                 [input_box, add_button],
                 [list_box,edit_button, complete_button],
                 [exit_button]]

window = sg.Window('My To-Do App',
                   layout=window_layout,
                   font=('Helvetica',12))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                selected_todo = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(selected_todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Try selecting a to-do before you click edit", font = ("helvetica", 12))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Try selecting a to-do before you click edit", font = ("helvetica", 12))
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()


