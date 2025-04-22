# 38. Use of super()
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car("Toyota", "Corolla")
car1.display()
