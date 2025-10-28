# 2. Custom Sort Function
# Implement bubble sort without using sort().
def sortitnow(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
numbers = int(input("Enter number of elements: "))
num_list = []
for _ in range(numbers):
    num_list.append(int(input("Enter number: ")))
sorted_list = sortitnow(num_list)
print("Sorted List:", sorted_list)

# Output:
# Enter number of elements: 5
# Enter number: 34
# Enter number: 12
# Enter number: 5
# Enter number: 78
# Enter number: 23
# Sorted List: [5, 12, 23, 34, 78] 