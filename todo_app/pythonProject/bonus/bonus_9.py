password = input('Enter a new password: ')
result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

is_digit = False
for i in password:
    if i.isdigit():
        is_digit = True
        break
result['Is_Digit'] = is_digit


is_upper = False
for i in password:
    if i.isupper():
        is_upper = True
        break
result['Is_Upper'] = is_upper


if all(result.values()):
    print('Strong Password')
else:
    print('Weak Password')