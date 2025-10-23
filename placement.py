age = int(input("Enter your age: "))
if age >= 22:
    regd = input("Enter your registration number: ")
    cgpa = float(input("Enter your CGPA: "))
    if cgpa > 6.5:
        marks_10 = float(input("Enter your 10th marks: "))
        marks_12 = float(input("Enter your 12th marks: "))
        print("You are allowed for placement.")
    else:
        print("CGPA is not sufficient for placement.")
else:
    print("Age is not sufficient for placement.")