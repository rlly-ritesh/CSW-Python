#tuple slicing 
wow = 1,4,2,5,6,14,'hello',"World" #tuple
print(type(wow))  #class tuple ( output )
print(wow)
#output
#(1, 4, 2, 5, 6, 14, 'hello', 'World')

print(wow[0])  #output 1 ( indexing )
print(wow[3])  #output 5 ( indexing )
print(wow[-1])  #output World ( indexing )
print(wow[1:5])  #output (4, 2, 5, 6) (slicing)
print(wow[2:])  #output (2, 5, 6, 14, 'hello', 'World') (slicing)
print(wow[:4])  #output (1, 4, 2, 5) (slicing)
print(wow[-4:])  #output (6, 14, 'hello', 'World') (slicing)
print(wow[:-3])  #output (1, 4, 2, 5, 6) (slicing)
print(wow[-6:-2])  #output (2, 5, 6, 14) (slicing)
print(wow[::2])  #output (1, 2, 6, 'hello') (slicing with step)
print(wow[1::2])  #output (4, 5, 14, 'World') (slicing with step)
print(wow[::-1])  #output ('World', 'hello', 14, 6, 5, 2, 4, 1) (reversing the tuple)
print(wow[-1::-1])  #output ('World', 'hello', 14, 6, 5, 2, 4, 1) (reversing the tuple)
print(wow[-2::-1])  #output (14, 6, 5, 2, 4, 1) (reversing the tuple except last element)
#wow[0] = 10  #error; tuple is immutable ( cannot be changed )
#TypeError: 'tuple' object does not support item assignment