def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(filepath, todos_local):
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


while True:
    user_text = input('Type add, edit, complete or show: ').strip()

    if user_text.startswith('add'):
        todo = user_text[4:] + '\n'

        todos = get_todos('todos.txt')

        todos.append(todo)

        write_todos('todos.txt', todos)

    elif user_text.startswith('show'):
        todos = get_todos('todos.txt')

        for i, j in enumerate(todos):
            print(f'{i + 1}. {j.strip('\n')}')

    elif user_text.startswith('edit'):
        try:
            todo_to_edit = int(user_text[5:]) - 1

            todos = get_todos('todos.txt')

            new_todo = input('Enter new todo: ')
            todos[todo_to_edit] = new_todo + '\n'

            write_todos('todos.txt', todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_text.startswith('complete'):
        try:
            completed_todo = int(user_text[9:]) - 1

            todos = get_todos('todos.txt')

            todos.pop(completed_todo)

            write_todos('todos.txt', todos)

        except IndexError:
            print('That item is out of range.')
            continue

    elif user_text.startswith('exit'):
        break
    else:
        print('Command is not valid.')
