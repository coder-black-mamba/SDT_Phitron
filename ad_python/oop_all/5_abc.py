"""
🔥 What Are Abstract Base Classes?
Abstract Base Classes (ABCs) are used to define interfaces (like a blueprint) that must be implemented by subclasses. You can't instantiate an ABC directly.

✅ Why Use ABCs?
Enforce a consistent API.

Prevent incomplete implementations.

Improve code maintainability and clarity.
"""
# abstract class == interface :) clear ? huh
from abc import ABC , abstractmethod,abstractproperty,abstractclassmethod,abstractstaticmethod
import math
import abc

# Basic Syntax

class BaseClass(ABC):
    # this is t
    @abstractmethod
    def my_method(self):
        pass



# example
"""
as like as interface we are jsut creating the skleliton like things
"""
class Shape(ABC):
    # later this method will be implemented in real class as a class method as it uses @abstractmethod
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Subclass . Basically Class From Interface
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    """
        without instantiation
        Traceback (most recent call last):
        File "/Users/abusayed/cs/SDT_Phitron/ad_python/oop_all/5_abc.py", line 50, in <module>
        rect1=Rectangle(5,2)
        TypeError: Can't instantiate abstract class Rectangle without an implementation for abstract methods 'area', 'perimeter'
    """

    def area(self):
        return  self.width*self.height

    def perimeter(self):
        return 2*(self.width+self.height)



# create instance [first e na kore dekhi  ki hoi]

rect1=Rectangle(5,2)
# print(rect1.area())
# print(rect1.perimeter())

# example 2 : circle

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


c1=Circle(5)
# print(c1.area())
# print(c1.perimeter())
print(dir(abc))


# ==================================== All abc usage =========================




class MyABC(ABC):
    @staticmethod
    @abstractmethod
    def my_static_method(): pass





"""
🧰 1. @abstractmethod
     Most commonly used.
    Forces a subclass to override this method.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# =============================================================================
"""
✅ Modern Way (Python 3.3+)
Instead of using:

@abstractclassmethod

@abstractstaticmethod

👉 Use this order instead:

✅ Abstract Class Method (Modern)
"""

class MyABC(ABC):
    @classmethod
    @abstractmethod
    def my_class_method(cls): pass


"""
✅ Abstract Static Method (Modern)
"""
# ====================================================================================

# 🧰 2. @abstractproperty (Deprecated!)
# 🛑 Note: @abstractproperty is deprecated since Python 3.3.
# Use @property + @abstractmethod instead.

# ❌ Deprecated Way:

from abc import ABC, abstractproperty

class Animal(ABC):
    @abstractproperty
    def species(self):
        pass


# Correct Way:

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass

class Dog(Animal):
    @property
    def species(self):
        return "Canine"





"""
🧰 3. @abstractclassmethod
Use this to define abstract class-level methods.
"""
class Student(ABC):
    @abstractclassmethod
    def show(cls):
        pass
    # @abstractclassmethod is also depricated use this below
    @classmethod
    @abstractmethod
    def show_info(cls):
        pass

class Sayed(Student):
    @classmethod
    def show(cls):
        print(cls)

    @classmethod
    def show_info(cls):
        print(cls)


Sayed.show()
Sayed.show_info()



# 🧰 4. @abstractstaticmethod
# Used for static methods that subclasses must implement.


class Animal(ABC):
    @abstractstaticmethod
    def kingdom():
        pass
    # @abstractstaticmethod is also depricated use this below
    @staticmethod
    @abstractmethod
    def kingdom():
        pass

class Dog(Animal):
    @staticmethod
    def kingdom():
        return "Animalia"

















