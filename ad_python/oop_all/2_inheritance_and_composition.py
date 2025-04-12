# just nothing but then tor father  features tui paichis

# ==================== Basic Inheritance ==============
# parent class
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Placeholder Methoad To Be Ovrridden BY Child Class")


# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, species):
        """ super() Function
            super() function is used to call the parent class’s methods.
             In particular, it is commonly used in the child class’s
             __init__() method to initialize inherited attributes.
             This way, the child class can leverage the functionality of the parent class.

        """
        super().__init__(name)
        self.species=species

    def speak(self):
        print(f"This is {self.species} {self.name} , Gheu Gheu")

# ======= using the class ======
dog = Dog("Kutta","Desi")


# dog.speak()

"""
Types of Python Inheritance
Single Inheritance: A child class inherits from one parent class.
Multiple Inheritance: A child class inherits from more than one parent class.
Multilevel Inheritance: A class is derived from a class which is also derived from another class.
Hierarchical Inheritance: Multiple classes inherit from a single parent class.
Hybrid Inheritance: A combination of more than one type of inheritance.

"""
# 1. Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

# 2. Multiple Inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job):  # Inherits from both Employee and Job
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, salary)            # Initialize Job

# 3. Multilevel Inheritance
class Manager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.department = department

# 4. Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, team_size):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.team_size = team_size

# 5. Hybrid Inheritance (Multiple + Multilevel)
class SeniorManager(Manager, AssistantManager):  # Inherits from both Manager and AssistantManager
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)        # Initialize Manager
        AssistantManager.__init__(self, name, salary, team_size)  # Initialize AssistantManager

# Creating objects to show inheritance

# Single Inheritance
emp = Employee("John", 40000)
print(emp.name, emp.salary)

# Multiple Inheritance
emp2 = EmployeePersonJob("Alice", 50000)
print(emp2.name, emp2.salary)

# Multilevel Inheritance
mgr = Manager("Bob", 60000, "HR")
print(mgr.name, mgr.salary, mgr.department)

# Hierarchical Inheritance
asst_mgr = AssistantManager("Charlie", 45000, 10)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size)

# Hybrid Inheritance
sen_mgr = SeniorManager("David", 70000, "Finance", 20)
print(sen_mgr.name, sen_mgr.salary, sen_mgr.department, sen_mgr.team_size)
