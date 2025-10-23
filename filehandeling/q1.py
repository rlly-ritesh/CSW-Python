# Writing to a text file
def writetextfile():
    file = open('sample.txt', 'w')  # Removed extra space and fixed quotes/parentheses
    file.write('Hello, World!\n')
    file.write('This is a text file.\n')
    file.write('Python file handling is easy!\n')  # Fixed closing quote
    file.close()
    print("*Text file created successfully!")

# Execute the function
writetextfile()