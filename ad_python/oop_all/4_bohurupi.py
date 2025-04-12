
# ============== polymorphism in built-in functions ==============
# print(len("Hello"))  # String length
# print(len([1, 2, 3]))  # List length
#
# print(max(1, 3, 2))  # Maximum of integers
# print(max("a", "z", "m"))  # Maximum in strings





# ============== polymorphism in built-in operators ==============

# print(5 + 10)  # Integer addition
# print("Hello " + "World!")  # String concatenation
# print([1, 2] + [3, 4])  # List concatenation

# ============== polymorphism in OOP ==============
# class Shape:
#     def area(self):
#         return "Undefined"
#
# class Reactangle(Shape):
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
#
#     def area(self):
#         return self.length*self.width
#
#
#
"""Ektai area method just ekek somoy ekek output dekhai etai polymorphism"""
class Shape:
    def area(self):
        return "Undefined"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(2, 3), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}")


"""
Compile-time Polymorphism
Found in statically typed languages like Java or C++, where the behavior of a function or operator is resolved during the program’s compilation phase.
Examples include method overloading and operator overloading, where multiple functions or operators can share the same name but perform different tasks based on the context.
In Python, which is dynamically typed, compile-time polymorphism is not natively supported. Instead, Python uses techniques like dynamic typing and duck typing to achieve similar flexibility.
Runtime Polymorphism
Occurs when the behavior of a method is determined at runtime based on the type of the object.
In Python, this is achieved through method overriding: a child class can redefine a method from its parent class to provide its own specific implementation.
Python’s dynamic nature allows it to excel at runtime polymorphism, enabling flexible and adaptable code.



"""