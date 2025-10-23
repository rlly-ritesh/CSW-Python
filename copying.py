import copy
from copy import deepcopy
# a = [10,20,30,40,50]
# reference = a
# print(f"Original list: {a}")
# copya = a.copy()
# print(f"Copy list: {copya}")

b = [[1,2,3], [4,5,6], [7,8,9]]
shallow_copy = b.copy()
deep = deepcopy(b)
shallow_copy[1][0] = 100
deep[0][0] = 200
print(f"Shallow copy of list: {shallow_copy}")
print(f"Deep copy of list: {deep}")