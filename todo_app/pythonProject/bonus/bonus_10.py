try:
    width = float(input('Enter a rectangle width: '))
    length = float(input('Enter rectangle length: '))

    if width == length:
        exit('That looks like a square.')

    area = width * length
    print(area)
except ValueError:
    print('please enter numeric values')