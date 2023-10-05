#importing the libraries
from collections import defaultdict

# This is base class
class Product:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available

# this is subclass. It inherits name, price, avaible from products
class ElectronicsProduct(Product):
    def __init__(self, name, price, available, quantity):
        super().__init__(name, price, available)
        self.quantity = quantity

# Creating Cart Class where all the necessary functionality are implemented
class Cart:
    def __init__(self):
        self.items = [] #empty list

    # Adding items to the cart
    def add_item(self, product, quantity):
        if quantity <= product.available:
            self.items.append({'product': product, 'quantity': quantity})
            product.available -= quantity
        else:
            print(f"Error: Quantity exceeds available stock for {product.name}.")

    # Updating items to the cart
    def update_quantity(self, product_name, new_quantity):
        for item in self.items:
            if item['product'].name == product_name:
                product = item['product']
                old_quantity = item['quantity']
                product.available += old_quantity  # Restore previous quantity
                item['quantity'] = new_quantity
                product.available -= new_quantity  # Deduct the updated quantity
                return

    #Removing items to the cart
    def remove_item(self, product_name):
        for item in self.items:
            if item['product'].name == product_name:
                product = item['product']
                quantity = item['quantity']
                product.available += quantity  # Restore available stock
        self.items = [item for item in self.items if item['product'].name != product_name]

    # Calculating total bill of the cart
    def calculate_total_bill(self):
        total_bill = 0
        for item in self.items:
            product = item['product']
            quantity = item['quantity']
            total_bill += product.price * quantity

        return total_bill

# Calculating total quantity of the cart
def calculate_total_quantities(cart):
    product_quantities = defaultdict(int)

    for item in cart.items:
        product = item['product']
        quantity = item['quantity']
        product_quantities[product.name] += quantity

    return dict(product_quantities)

# Sample products available
laptop = ElectronicsProduct("Laptop", 1000, 5, 12)
headphones = ElectronicsProduct("Headphones", 50, 10, 6)
mobile = ElectronicsProduct("Mobile", 10000, 2, 10)

# Creating a dictionary to map user input to product instances
products = {
    "laptop": laptop,
    "headphones": headphones,
    "mobile": mobile
}

# This main function sets up the shopping cart and enters a loop for user interaction,
# displaying menu options for the user to perform cart-related actions.
def main():
    cart = Cart()
    while True:
        print("1. Add to Cart")
        print("2. Update Quantity")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Calculate Total Bill")
        print("6. Quit")
        choice = input("Enter your choice: ")

        # Adding the product to cart
        if choice == "1":
            product_name = input("Enter the product name to add to the cart: ").lower()
            if product_name in products:
                product = products[product_name]
                quantity = int(input("Enter the quantity: "))

                cart.add_item(product, quantity)
                print(f"{quantity} {product_name.capitalize()}(s) added to the cart.")
            else:
                print("Error: Product not found.")

        # Updating the product to cart
        elif choice == "2":
            product_name = input("Enter the product name to update quantity: ").lower()
            if product_name in products:
                new_quantity = int(input("Enter the new quantity: "))
                cart.update_quantity(products[product_name].name, new_quantity)
                print(f"Quantity updated for {product_name.capitalize()} to {new_quantity}.")
            else:
                print("Error: Product not found.")

        # Removing the product to cart
        elif choice == "3":
            product_name = input("Enter the product name to remove from the cart: ").lower()
            if product_name in products:
                cart.remove_item(products[product_name].name)
                print(f"{product_name.capitalize()} removed from the cart.")
            else:
                print("Error: Product not found in the cart.")

        # Viewing the products in cart
        elif choice == "4":
            if not cart.items:
                print("Cart is empty.")
            else:
                print("Cart Contents:")
                for item in cart.items:
                    product = item['product']
                    quantity = item['quantity']
                    print(f"{quantity} {product.name}(s) at ${product.price} each")

                #calculating total quantities added to cart
                total_quantities = calculate_total_quantities(cart)
                for product_name, total_quantity in total_quantities.items():
                    print(f"Total {product_name.capitalize()}s: {total_quantity}")

        #calculating the total bill of cart
        elif choice == "5":
            total_bill = cart.calculate_total_bill()
            print(f"Total Bill: Your total bill is ${total_bill}.")

        #exit condition
        elif choice == "6":
            break

        else:
            print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
