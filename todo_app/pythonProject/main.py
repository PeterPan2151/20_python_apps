while True:
    user_text = input('Type add, edit, complete or show: ').strip()
    
    match user_text:
        case 'add':
            todo = input('Enter a todo: ') + '\n'

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for i, j in enumerate(todos):
                print(f'{i + 1}. {j.strip('\n')}')

        case 'edit':
            todo_to_edit = int(input('What number todo do you want to edit? '))
            new_todo = input('Enter new todo: ')
            todos[todo_to_edit - 1] = new_todo
        case 'complete':
            completed_todo = int(input('What number todo have you completed? '))
            todos.pop(completed_todo - 1)
        case 'exit':
            break
