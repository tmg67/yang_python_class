from abc import ABC , abstractmethod 
class Vehicle(ABC):# ABC id abstract base class
    @abstractmethod
    def drive(self):
        print("vehicle is driving")
        #pass
    def new_fn(self):
        print("my new fn")
class Car(Vehicle):
    pass
    # def drive(self)
    # return "car is driving"
# example 6; using abstraction
car = Car()
print(car.drive()) # output : car is driving

#veh = Vehicle()
#print(veh.drive()) # access abstract method 