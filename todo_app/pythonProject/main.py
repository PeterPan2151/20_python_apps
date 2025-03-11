todos = []
while True:
    user_text = input('Type add or show: ')
    match user_text:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(user_text)
        case 'show':
            for i in todos:
                print(i)
        case 'exit':
            break
