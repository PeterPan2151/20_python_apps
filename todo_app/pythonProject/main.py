def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_local, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


while True:
    user_text = input('Type add, edit, complete or show: ').strip()

    if user_text.startswith('add'):
        todo = user_text[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_text.startswith('show'):
        todos = get_todos()

        for i, j in enumerate(todos):
            print(f'{i + 1}. {j.strip('\n')}')

    elif user_text.startswith('edit'):
        try:
            todo_to_edit = int(user_text[5:]) - 1

            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[todo_to_edit] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_text.startswith('complete'):
        try:
            completed_todo = int(user_text[9:]) - 1

            todos = get_todos()

            todos.pop(completed_todo)

            write_todos(todos)

        except IndexError:
            print('That item is out of range.')
            continue

    elif user_text.startswith('exit'):
        break
    else:
        print('Command is not valid.')
