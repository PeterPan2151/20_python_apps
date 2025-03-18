while True:
    user_text = input('Type add, edit, complete or show: ').strip()

    if 'add' in user_text:
        todo = user_text[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_text:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for i, j in enumerate(todos):
            print(f'{i + 1}. {j.strip('\n')}')

    elif 'edit' in user_text:
        todo_to_edit = int(user_text[5:]) - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input('Enter new todo: ')
        todos[todo_to_edit] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_text:
        completed_todo = int(user_text[9:]) - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(completed_todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'exit' in user_text:
        break
    else:
        print('Command is not valid.')
