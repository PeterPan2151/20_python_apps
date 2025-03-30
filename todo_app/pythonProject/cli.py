from functions import get_todos, write_todos
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print(f'It is {now}')
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
