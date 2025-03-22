def parse(feet_inches_local):
    feet, inches = feet_inches_local.split()
    feet = float(feet)
    inches = float(inches)
    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input('Enter feet and inches: ')
f, i = parse(feet_inches)

result = convert(f, i)

if result < 1:
    print('Kid is too small')
else:
    print('Kid can use the slide')
