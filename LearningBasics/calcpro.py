import math

def askp(result):
    ch = input("Apply ceiling, floor, hexadecimal, binary, octal, or none? (c/f/h/b/o/n): ")
    if ch == 'c':
        print("Result (ceiling):", math.ceil(result))
    elif ch == 'f':
        print("Result (floor):", math.floor(result))
    elif ch == 'h':
        print("Result (hexadecimal):", hex(int(result)))
    elif ch == 'b':
        print("Result (binary):", bin(int(result)))
    elif ch == 'o':
        print("Result (octal):", oct(int(result)))
    else:
        print("Result:", result)

def calcpro():
    print("Calculator PRO")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /, %, //, ^, percentage): ")
    result = None

    if op == '+':
        result = num1 + num2
        askp(result)
    elif op == '-':
        result = num1 - num2
        askp(result)
    elif op == '*':
        result = num1 * num2
        askp(result)
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
            askp(result)
        else:
            print("Error! Division by zero.")
    elif op == '%':
        result = num1 % num2
        askp(result)
    elif op == '//':
        if num2 != 0:
            result = num1 // num2
            askp(result)
        else:
            print("Error! Division by zero.")
    elif op == '^':
        result = num1 ** num2
        askp(result)
    elif op.lower() == 'percentage':
        if num1 != 0:
            percent = (num2 / num1) * 100
            print(f"{num2} is {percent:.2f}% of {num1}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation.")

calcpro()
