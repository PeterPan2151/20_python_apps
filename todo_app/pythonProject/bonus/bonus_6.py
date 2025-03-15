contents = ['All carrots are to be sliced longitudinally',
            'The carrots were reportedly sliced.',
            'The slicing process was well presented.']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, file in zip(contents, filenames):
    file = open(f'../files/{file}', 'w')
    file.write(content)
    file.close()
