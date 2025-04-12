"""
Protected members
Protected members are identified with a single underscore (_). They are meant to be accessed only within the class or its subclasses.

"""
class Bedi_Manush:
    def __init__(self,age,bf):
        # protected
        self._age=age
        # private
        self.__bf=bf

class Fahmida(Bedi_Manush):
    def disp_age(self):
        # print(self._age,self._Bedi_Manush__bf)
        print(self._age)

obj1=Fahmida(18,"Husband")
# obj1.disp_age()

# obj2 with bedi manush
eva= Bedi_Manush(22,"Shuvo")
# should not use as it is a protected method
# it is a convention starting with _ means we have no business with it
# print(eva._age)

# you can access private things by self.[_classname__privatevariable]
# print(dir(obj1))

"""
Private members
Private members are identified with
 a double underscore (__) and cannot be accessed directly from outside the class. 
 Python uses name mangling to make private members inaccessible by renaming them internally.

Note: Python’s private and protected members can be accessed outside the class through python name mangling. 
"""

class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    # getter
    # def salary(self):
    #     return self.__salary  # Access through public method
    # setter
    # def set_salary(self,salary):
    #     self.__salary=salary


    # the pythonic way of getter setter
    @property
    def salary(self):
        """Getter For Salary"""
        return self.__salary

    @salary.setter
    def salary(self,salary):
        self.__salary=salary



obj = Private()
# print(obj.salary())  # Works
# obj.set_salary(100)
# print(obj.salary())  # Works

# print(obj.__salary)  # Raises AttributeError
# but can be access through this
#  can access variable things by self.[_classname__varibalename]

# print(obj._Private__salary) #outputs same bu bad practise

# pythonic way of getter setter
print(obj.salary)
obj.salary=200
print(obj.salary)
