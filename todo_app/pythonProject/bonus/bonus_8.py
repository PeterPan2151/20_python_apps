date = input('Enter today \'s date: ')
mood = input('How do you rate your mood from 1 to 10? ')
journal_text = input('Let your thoughts flow: ')

with open(f'../journal/{date}.txt', 'w') as file:
    file.write(mood + 2 * '\n')
    file.write(journal_text)

