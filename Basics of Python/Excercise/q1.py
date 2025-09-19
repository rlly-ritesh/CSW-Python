#Write a program that takes two numbers as input and prints their sum, difference,
#product, and quotient.
def calculate():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    diff = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    print("Sum:", sum)
    print("Difference:", diff)
    print("Product:", product)
    print("Quotient:", quotient)
    print("Remainder:", num1 % num2)

calculate()