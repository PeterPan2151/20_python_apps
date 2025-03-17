while True:
    user_text = input('Type add, edit, complete or show: ').strip()
    
    match user_text:
        case 'add':
            todo = input('Enter a todo: ') + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for i, j in enumerate(todos):
                print(f'{i + 1}. {j.strip('\n')}')

        case 'edit':
            todo_to_edit = int(input('What number todo do you want to edit? ')) - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input('Enter new todo: ')
            todos[todo_to_edit] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            completed_todo = int(input('What number todo have you completed? ')) - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(completed_todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break
