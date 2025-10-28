#conversion of lower data type Integer ( Int ) to higher data type Float ( Float )
a = 5
b = float(a) #typecasting
print(b)
print(type(b))  #class float ( output )

#Explicit Type Conversion
# In Explicit Type Conversion, users convert the data type of an object to required data type.
# We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.
# This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

num_string = '123'
num_int =  23
num_string = int(num_string)  #typecasting
print(num_string + num_int)  #output 146
print(type(num_string))  #class int ( output )