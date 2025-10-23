def fun():
    str1 = input("enter a string")
    str2 = input("enter a string2")
    str3 = str1+""+str2
    str4 = str3.replace("o","0")
    print(f"final string : {str4} ")
    length = len(str4)
    binary = bin(length)
    print(binary)
fun()
    