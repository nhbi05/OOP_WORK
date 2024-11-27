import math
"""class Employee:
    def __init__(self,salary):
        self.salary= salary

    def get_salary(self):
        return 1000

class Manager(Employee):
    def get_salary(self):
        return super().get_salary()

sal1=Employee(2000)
sal2=Manager(3000)
print(sal1.get_salary())
print(sal2.get_salary())"""

"""class Shape:
    def area(self,Area):
        return self.Area

class Rectangle(Shape):
    def area(self,length,width):
        self.length=length
        self.width=width
        rect_area= self.length*self.width
        return rect_area

class Circle(Shape):
   def area(self,radius):
        self.radius=radius
        circle_area= math.pi*(radius**2)
        return circle_area
   
circle1=Circle()
rect1=Rectangle()
print(circle1.area(300))
print(rect1.area(300,80))"""

class Vehicle:
    def max_speed(self):
        return 100
class Car(Vehicle):
    def max_speed(self):
        return 180
class Bike(Vehicle):
    def max_speed(self):
        return 120
    
car1= Car()
veh1=Vehicle()
bike1=Bike()
print(car1.max_speed())
print(veh1.max_speed())
print(bike1.max_speed())

