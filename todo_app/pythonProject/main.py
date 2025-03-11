todos = []
while True:
    user_text = input('Type add, edit or show: ').strip()
    match user_text:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show':
            for i, j in enumerate(todos):
                print(f'{i + 1}. {j}')
        case 'edit':
            todo_to_edit = int(input('What number todo do you want to edit? '))
            new_todo = input('Enter new todo: ')
            todos[todo_to_edit - 1] = new_todo
        case 'exit':
            break
