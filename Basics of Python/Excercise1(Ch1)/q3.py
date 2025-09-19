#Write a program that stores 5 names in a list, sorts them, and prints the sorted list.
def sort_names():
    while True:
        names = []
        for i in range(5):
            name = input(f"Enter name {i+1}: ")
            names.append(name)
        names.sort()
        print("Sorted names:", names)
sort_names()