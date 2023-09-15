class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def get_info(self):
        print(f'{self.brand} {self.model} {self.year} {self.price}')


class Car(Vehicle):
    def __init__(self, brand, model, year, price, doors, style):
        super().__init__(brand, model, year, price)
        self.doors = doors
        self.style = style

    def get_detailed_info(self):
        print(f'{self.brand} {self.model} {self.year} {self.price} {self.doors} {self.style}')


car1 = Car('Tesla', 'Model S', '2015', '80000$', 5, 'sedan')
car1.get_info()
car1.get_detailed_info()

car2 = Car('Tesla', 'Model 3', '2020', '40000$', 5, 'sedan')
car2.get_info()
car2.get_detailed_info()
