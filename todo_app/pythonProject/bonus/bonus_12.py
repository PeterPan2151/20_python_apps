def convert(feet_inches_local):
    feet, inches = feet_inches_local.split()
    feet = float(feet)
    inches = float(inches)
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input('Enter feet and inches: ')
result = convert(feet_inches)

if result < 1:
    print('Kid is too small')
else:
    print('Kid can use the slide')
