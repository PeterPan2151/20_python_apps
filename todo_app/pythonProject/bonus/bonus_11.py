def get_average():
    with open('../files/data.txt', 'r') as file:
        data = file.readlines()

    numbers = [float(i) for i in data[1:]]
    average_local = sum(numbers) / len(numbers)
    return average_local

average = get_average()
print(average)
