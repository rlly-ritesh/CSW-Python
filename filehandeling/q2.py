def writetextfile():
    with open('sample.txt', 'w') as file:
        file.write('Hello, World!\n')
        file.write('This is a text file.\n')
        file.write('Python file handling is easy!\n')
    print("*Text file created successfully!")
    