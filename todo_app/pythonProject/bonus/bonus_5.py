waiting_list = ['sen', 'ben', 'john']

for spot, name in enumerate(sorted(waiting_list)):
    print(f'{spot + 1}.{name.capitalize()}')
