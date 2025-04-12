# day 1 of oop
# defination of class
"""
✅ 1. What is a Class and Object?
Class: A blueprint for creating objects (a custom data type).

Object: An instance of a class.

"""



class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.price=price
        self.price=price
    # Self Parameter




class Dog:


    # class initiator
    def __init__(self,name,age):
        self.name=name
        self.age=age


    # instance method
    def bark(self):
        print(f"{self.name} gheu gheu kore")

    # testing self __str__ have to default one
    def test_self(self):
        # self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.
        return self



    # dunder methods
    # __str__
    def __str__(self):
        return f"Name : {self.name} \nAge: {self.age}"






# ===================== using the classes ====================
kutta = Dog("Honey",12)
# kutta.bark()
# print("Kuttar Baccha Futfute Shundor ")
# print(Dog)
# print(kutta)


# ========================== checking self =====================
# kutta is the instance of the class now the test self function and the address of the kutta should be the same if thisare the same this means self represents the class itself . __str__ have to be the default one

# print(kutta)
# print(kutta.test_self())

# ================= Class and Instance Variables in Python==========

"""
In Python, variables defined in a class can be either class variables or instance variables, and understanding the distinction between them is crucial for object-oriented programming.

Class Variables
These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods. All objects of the class share the same value for a class variable unless explicitly overridden in an object.

Instance Variables
Variables that are unique to each instance (object) of a class. These are defined within __init__ method or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.

"""


class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)


"""
Explanation:

Class Variable (species): Shared by all instances of the class. Changing Dog.species affects all objects, as it’s a property of the class itself.
Instance Variables (name, age): Defined in the __init__ method. Unique to each instance (e.g., dog1.name and dog2.name are different).
Accessing Variables: Class variables can be accessed via the class name (Dog.species) or an object (dog1.species). Instance variables are accessed via the object (dog1.name).
Updating Variables: Changing Dog.species affects all instances. Changing dog1.name only affects dog1 and does not impact dog2.


"""
