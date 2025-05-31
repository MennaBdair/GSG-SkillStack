class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price:.2f}")

class Drink(Product):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = int(volume)

    def display_info(self):
        super().display_info()
        print(f"Volume: {self.volume}ml")

class Snack(Product):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = int(calories)

    def display_info(self):
        super().display_info()
        print(f"Calories: {self.calories}")

class Candy(Product):
    def __init__(self, name, price, flavor):
        super().__init__(name, price)
        self.flavor = flavor

    def display_info(self):
        super().display_info()
        print(f"Flavor: {self.flavor}")
