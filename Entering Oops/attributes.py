class circle:
    pi=3.14159
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return circle.pi*self.radius**2
circle1 = circle(5)
circle2 = circle(10)

print(f"Circle 1 area : {circle1.area():.2f}")
print(f"Circle 2 Area : {circle2.area():.2f}")
#Circle 1 area : 78.58
#Circle 2 Area : 314.16
#Pi Value : 3.14159
