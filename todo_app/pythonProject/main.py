while True:
    user_text = input('Type add, edit, complete or show: ').strip()

    if user_text.startswith('add'):
        todo = user_text[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_text.startswith('show'):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for i, j in enumerate(todos):
            print(f'{i + 1}. {j.strip('\n')}')

    elif user_text.startswith('edit'):
        try:
            todo_to_edit = int(user_text[5:]) - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input('Enter new todo: ')
            todos[todo_to_edit] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_text.startswith('complete'):
        try:
            completed_todo = int(user_text[9:]) - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(completed_todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print('That item is out of range.')
            continue

    elif user_text.startswith('exit'):
        break
    else:
        print('Command is not valid.')
