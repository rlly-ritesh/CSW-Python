#Create a function that checks if a number is even or odd.
def check_numbr():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")
check_numbr()
    