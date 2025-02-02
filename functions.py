FILEPATH = 'todos.txt'



def get_todos(filepath=FILEPATH):
    """ Open the text file located at filepath, and read the file line by line to a list
    :param filepath: type=String; Path to todos.txt
    :return: type=list; a list of todo items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todo_arg, filepath=FILEPATH):
    """ write the todos list to the text file located at filepath
    :param todo_arg: type=list; the newest version of the todo list
    :param filepath: type=String; path to todo text file
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)



if __name__ == "__main__":
    print(get_todos())