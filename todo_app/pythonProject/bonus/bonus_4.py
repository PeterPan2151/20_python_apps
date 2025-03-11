filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentation.txt']
new_files = []
for file in filenames:
    new_files.append(file.replace('.', '-', 1))

print(new_files)