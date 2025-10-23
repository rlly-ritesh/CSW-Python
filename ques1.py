# #Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
def areac():
    length = int(input("Enter length of the field"))
    width = int(input("Enter width of the field"))
    area = 43560*length*width
    print(f"Area in acers : {area}")
areac()