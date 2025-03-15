filenames = ['1.doc.txt', '1.report.txt', '1.presentation.txt']
new_files = [i.replace('.', '-', 1) for i in filenames]
print(new_files)
