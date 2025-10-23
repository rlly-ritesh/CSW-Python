class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says Woof!"
    def get_age(self):
        return f"{self.name} is {self.age} years old"
# Creating instances (objects)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
# Using methods
print(dog1.bark())
print(dog2.get_age())