# Function: Write a python class to represent a vector. Implement the following behaviour in your vector class:
# (a). vector addition.
# (b). vector multiplication by an int.
# (c). vector subtraction.
# (d). vector multiplication by another vector.
# (e). vector magnitude.
#
# Author: Scott Donnelly
# Date: 06/12/2018

# Compiler used: PyCharm

import math  # Necessary for the Sqrt() function.

# Functions/Classes
class Vectors:
    def __init__(self, V1x, V1y, V2x, V2y):
        self.V1x = V1x
        self.V1y = V1y
        self.V2x = V2x
        self.V2y = V2y

    def __info__(self):
        return self.V1x, self.V1y, self.V2x, self.V2y


	def addition():
		coords = Vectors(V1x, V2x, V1y, V2y)
		new_vecx = (coords.V1x + coords.V2x)
		new_vecy = (coords.V1y + coords.V2y)

		print("The addition of V1 and V2 is (", new_vecx, ",", new_vecy, ")")

	def mulint(self, V1x, V1y):
		n = input("Please enter an int that you want to use for the multiplication.\n")
		n = int(n) # making sure the user input is an int

		Vxnx = V1x*n  # This is the multiplication process.
		Vxny = V1y*n

		print("The multiplication of V1 by", n, "is", "(", Vxnx, ",", Vxny, ")")

	def subtraction(self, V1x, V1y, V2x, V2y):
		new_vecx = (V1x - V2x)
		new_vecy = (V1y - V2y)

		print("The subtraction of V1 and V2 is (", new_vecx, ",", new_vecy, ")")

	def mulvec(self, V1x, V1y, V2x, V2y):
		xs = (V1x*V2x)
		ys = (V1y*V2y)

		V1byV2 = (xs + ys)

		print("The multiplication of V1 by V2 is", V1byV2,)

	def magnitude(self, V1x, V1y):
		# V = SquareRoot(X^2 + Y^2)
		xsquared = (V1x*V1x)
		ysquared = (V1y*V1y)
		V = xsquared + ysquared
		V = math.sqrt(V)

		print("The magnitude of V1 is", V, )

# Main function
def main():
    # Declaring variables. Im using seperate interger variables for each element of the coordinates
    V1x = 3
    V1y = 2
    V2x = 4
    V2y = 1

    # Menu to choice which function you want
    print("\n1. Addition.")
    print("2. Multiplication by int.")
    print("3. Subtraction.")
    print("4. Multiplication by another vector.")
    print("5. Magnitude.")
    print("\nVector 1 is (", V1x, ",", V1y, ")")
    print("\nVector 2 is (", V2x, ",", V2y, ")")

    while 1:  # This loop allows you to keep the program running to go through all the options
        choice = input("\nPlease enter the number that corresponds to what option you want: ")
        choice = int(choice)  # making the variable a int

        if choice == 1:
            # Call function
            Vectors.addition()

        elif choice == 2:
            Vectors.mulint(V1x, V1y)

        elif choice == 3:
            Vectors.subtraction(V1x, V1y, V2x, V2y)

        elif choice == 4:
            Vectors.mulvec(V1x, V1y, V2x, V2y)

        elif choice == 5:
            Vectors.magnitude(V1x, V1y)

        else:
            print("Invalid input! Please enter a valid number that corresponds to an option on the menu.\n")

main()