from menu_item import MenuItem
from order import Order

class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def add_order(self, order):
        self.orders.append(order)

    def list_orders(self):
        for i, order in enumerate(self.orders, start=1):
            print(f"Order {i}:")
            print(order)
            print()