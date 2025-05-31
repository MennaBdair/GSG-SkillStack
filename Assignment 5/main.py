from product import Product, Drink, Snack, Candy

def load_products(filename):
    products = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if not parts or len(parts) < 4:
                continue
            type_, name, price, attr = parts
            if type_ == 'Drink':
                products.append(Drink(name, price, attr))
            elif type_ == 'Snack':
                products.append(Snack(name, price, attr))
            elif type_ == 'Candy':
                products.append(Candy(name, price, attr))
    return products

def display_menu(products):
    print("Welcome to the Python Vending Machine!")
    print("Please select what you want:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.__class__.__name__} - {product.name}")
    choice = int(input("> "))
    if 1 <= choice <= len(products):
        print("\nProduct Information:")
        products[choice - 1].display_info()
    else:
        print("Invalid selection.")

if __name__ == '__main__':
    products = load_products('products.txt')
    display_menu(products)
