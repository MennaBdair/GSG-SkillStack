from menu_item import MenuItem

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        order_details = "\n".join([f"- {item}" for item in self.items])
        return f"{order_details}\nTotal: ${self.total():.2f}"