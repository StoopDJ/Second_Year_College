# Function:
# 1. Write a class to represent an Item - each item has name, price and quantity.
# Include a method to calculate total price. Test your class by creating few Item objects.
# 2. Write a class to represent a complex number.
# Complex numbers can be written in the form of a+bi where a and b are real numbers and i is the solution of i^2=-1
#
# Add methods to add and subtract complex numbers - to add/subtract complex numbers you add/subtract
# the corresponding real and imaginary parts.
#
# For example, adding 1+2i and 2+3i will result in 3+5i
# Compiler used: PyCharm

# Functions/Classes

class Items:

    def __init__(self, name, price, quantity):  # Initialise the variables.
        self.name = name
        self.price = price
        self.quantity = quantity

    def __info__(self):
        return self.name, self.price, self.quantity,


def Stock(new_cart): #  Function to add an item to the parameters defined in the class.
             # This way the user can add their own items during run-time
    name_ = input("Please enter the item name.\n")
    price_ = input("Please enter the item price.\n")
    quantity_ = input("Please enter the item quantity.\n")

    new_item = Items(name_, price_, quantity_)
    print(new_item.name, "Has been added to your basket.\n")

    quantity_ = int(quantity_)
    price_ = int(price_)
    cart = price_ * quantity_
    new_cart = (new_cart + cart)
    print("Your basket is: €", new_cart)

# Main function
def main():
    new_cart = 0

    # Menu to choice which function you want
    print("1. Add items to the class.\n")
    print("2. View you cart.\n")

    while 1:
        choice = input("\nPlease enter the number that corresponds to what option you want:\n")
        choice = int(choice)  # making the variable an int

        if choice == 1:
        # Call function
            Stock(new_cart)

        #  elif choice == 2:

        else:
            print("Invalid input\n")

main()
