A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
 
# Set union using .union()
print(A.union(B))
# Set union using the | operator
print(A | B)
# Output:
# {1, 2, 3, 4, 5, 6, 8}
print(A.intersection(B))
# Use the & operator
print(A & B) 
# Output:
# {1, 2, 4}
print(A.difference(B))
# Use the - operator
print(A - B)
# Output:
# {8, 6}
print(B.difference(A))
# Use the - operator
print(B - A)
# Output:
# {3, 5}