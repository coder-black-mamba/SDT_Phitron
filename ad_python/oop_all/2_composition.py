# engine object
class Engine:
    def __init__(self,hp):
        self.hp=hp
    def start(self):
        print(f"{self.hp} Engine Started ->")
    def stop(self):
        print(f"{self.hp} Engine stopped <-")




# Base class
class Vehicle:
    def __init__(self, make, model ,engine : Engine):
        self.make = make
        self.model = model
        self.engine=engine

    def start(self):
        print(f"{self.make} {self.model} is starting.")
        self.engine.start()

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")
        self.engine.stop()


# Derived classes
class Car(Vehicle):
    def open_trunk(self):
        print("Opening the car trunk.")

class Truck(Vehicle):
    def load_cargo(self):
        print("Loading cargo into the truck.")


# now with engine
v8_engine=Engine(400)
eco_engine = Engine(150)


# before composition

# my_car = Car("Toyota", "Corolla",)
# my_car.start()
# my_car.open_trunk()
#
# my_truck = Truck("Ford", "F-150")
# my_truck.start()
# my_truck.load_cargo()

my_car = Car("Toyota", "Corolla", eco_engine)
my_car.start()
my_car.open_trunk()
my_car.stop()

my_truck = Truck("Ford", "F-150", v8_engine)
my_truck.start()
my_truck.load_cargo()
my_truck.stop()
