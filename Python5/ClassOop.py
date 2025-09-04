class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model  #Attributes

    def drive(self): #Method
        print(f"{self.brand} {self.model} is being driven by Joelina")

#Creating an object

plp_car = Car("Toyota","Altez")
plp_car.drive()

# Defining a class
class Car:
    color = "red"  # Attribute

    # Method
    def drive(self):
        print("The car is driving 🚗")

# Creating an object
my_car = Car()
print(my_car.color)
my_car.drive()