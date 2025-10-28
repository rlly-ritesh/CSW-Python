#this is an example for nested dictionary
students = {
    "101": {"name": "Alice", "age": 20, "marks": {"math": 85, "science": 90}},
    "102": {"name": "Bob", "age": 22, "marks": {"math": 78, "science": 88}},
}
#here  101 is main  key and name, age, marks are sub keys  same for 102; 
# Accessing nested values
print(students["101"]["name"])         # Output: Alice
print(students["102"]["marks"]["math"]) # Output: 78
