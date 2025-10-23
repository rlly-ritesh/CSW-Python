class Person:
    def __init__(self,name):
        self.name = name
person = Person("Alice")
print(f"Name : {person.name}")
#adding new instance variable dynamically
person.age = 30
person.city="New York"
print(f"Age:{person.age}")

