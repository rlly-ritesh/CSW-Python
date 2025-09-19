#Create a dictionary to store 3 students’ names and grades, then print each student’s information.
def print_students():
    my_dict = {}

    while True:
        key = input("Enter a Name (or 'done' to finish): ")
        if key == 'done':
            break
        value = input(f"Enter the value for '{key}': ")
        my_dict[key] = value
        print(my_dict)

print_students()