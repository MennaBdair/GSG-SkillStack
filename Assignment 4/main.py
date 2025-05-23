from menu_item import MenuItem
from order import Order
from restaurant import Restaurant

def display_menu(menu):
    if not menu:
        print("The menu is empty.")
    else:
        print("Menu:")
        for i, item in enumerate(menu, start=1):
            print(f"{i}. {item}")

def main():
    restaurant = Restaurant()

    while True:
        print("\nWelcome to the Restaurant Management System!")
        print("Choose an option:")
        print("1. Add menu item")
        print("2. View menu")
        print("3. Create new order")
        print("4. List all orders")
        print("5. Exit")
        choice =int(input("> "))

        if choice == 1:
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            category = input("Enter item category: ")
            item = MenuItem(name, price, category)
            restaurant.add_menu_item(item)
            print("Menu item added successfully.")
        elif choice == 2:
            display_menu(restaurant.menu)
        elif choice == 3:
            display_menu(restaurant.menu)
            if restaurant.menu:
                indices = input("Enter item numbers for the order separated by commas (e.g., 1,2): ")
                indices = [int(i.strip()) - 1 for i in indices.split(",")]
                order = Order()
                for idx in indices:
                    if 0 <= idx < len(restaurant.menu):
                        order.add_item(restaurant.menu[idx])
                restaurant.add_order(order)
                print("Order created and added successfully.")
        elif choice == 4:
            print("Orders:")
            restaurant.list_orders()
        elif choice == 5:
            print("Thank you for using the Restaurant Management System!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()