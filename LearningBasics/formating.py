# Example: Using different specifiers
value = 42
print("Integer : %d , Hex : %x , Octal : %o" % (value, value, value))
# % Percent Sign Variable-Length Print Fields
print ("Name : %-10s Age : %5d" % ("Alice",25))
#THE GLOBAL FORMAT FUNCTION
print(format(42,"d"),format(42,"x"),format(3.14159,".2f"))
#Format Method
name = "BOB"
age = 30
print("Name: {} , Age: {}".format(name,age))
#Ordering By Position (Name or Number)
print("{1},{0}".format("first","second"))
