
# Restaurant Ordering System
# CYB 301 - Object-Oriented Programming Project

# Class 1: Restaurant
class Restaurant:
    def __init__(self, name):
        # Initialize the restaurant name and menu
        self.name = name
        self.menu = {
            1: ("Burger", 8.99),
            2: ("Pizza", 10.99),
            3: ("Fries", 3.49),
            4: ("Soda", 1.99)
        }

    def display_menu(self):
        # Display all available food items and prices
        print("\n========== MENU ==========")
        for number, item in self.menu.items():
            name, price = item
            print(f"{number}. {name} - ${price:.2f}")
        print("5. Finish Order")

    def take_order(self, order):
        # Allow the customer to select multiple items
        while True:
            self.display_menu()

            try:
                choice = int(input("\nChoose an item:  "))

                # Stop taking orders when the customer chooses 5
                if choice == 5:
                    break

                # Check whether the selected item exists
                if choice not in self.menu:
                    print("Invalid selection. Please try again.")
                    continue

                quantity = int(input("Enter quantity: "))

                # Make sure the quantity is positive
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                # Add the selected item to the order
                name, price = self.menu[choice]
                order.add_item(name, price, quantity)

                print(f"Added {quantity} {name}(s) to your order!")

            except ValueError:
                print("Please enter a valid whole number.")


# Class 2: Order
class Order:
    def __init__(self):
        # Initialize an empty order
        self.items = []
        self.total = 0.0

    def add_item(self, name, price, quantity):
        # Store the selected food item and quantity
        self.items.append((name, price, quantity))

    def calculate_total(self):
        # Calculate the total cost of all ordered items
        self.total = 0.0

        for name, price, quantity in self.items:
            self.total += price * quantity

        return self.total

    def display_receipt(self):
        # Print the customer's receipt
        print("\n========== YOUR RECEIPT ==========")

        if not self.items:
            print("You did not order anything.")
            return

        for name, price, quantity in self.items:
            subtotal = price * quantity
            print(
                f"{quantity} x {name} - ${subtotal:.2f}"
            )

        # Display the final amount
        print("----------------------------------")
        print(f"Total: ${self.calculate_total():.2f}")
        print("Thank you for ordering!")


# Main program
def main():
    # Create the restaurant and order objects
    restaurant = Restaurant("Althea's Restaurant")
    customer_order = Order()

    print(f"Welcome to {restaurant.name}!")

    # Let the restaurant interact with the order object
    restaurant.take_order(customer_order)

    # Display the completed order and final bill
    customer_order.display_receipt()


# Start the program
if __name__ == "__main__":
    main()
