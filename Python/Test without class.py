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
    
def addition(V1x, V1y, V2x, V2y):
	new_vecx = (V1x + V2x)
	new_vecy = (V1y + V2y)

	print("The addition of V1 and V2 is (", new_vecx, ",", new_vecy, ")")

def mulint(V1x, V1y):
	n = input("Please enter an int that you want to use for the multiplication.\n")
	n = int(n) # making sure the user input is an int

	Vxnx = V1x*n  # This is the multiplication process.
	Vxny = V1y*n

	print("The multiplication of V1 by", n, "is", "(", Vxnx, ",", Vxny, ")")

def subtraction(V1x, V1y, V2x, V2y):
	new_vecx = (V1x - V2x)
	new_vecy = (V1y - V2y)

	print("The subtraction of V1 and V2 is (", new_vecx, ",", new_vecy, ")")
	
def mulvec(V1x, V1y, V2x, V2y):
	xs = (V1x*V2x)
	ys = (V1y*V2y)

	V1byV2 = (xs + ys)

	print("The multiplication of V1 by V2 is", V1byV2,)

def magnitude(V1x, V1y):
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
            addition(V1x, V1y, V2x, V2y)

        elif choice == 2:
            mulint(V1x, V1y)

        elif choice == 3:
            subtraction(V1x, V1y, V2x, V2y)

        elif choice == 4:
            mulvec(V1x, V1y, V2x, V2y)

        elif choice == 5:
            magnitude(V1x, V1y)

        else:
            print("Invalid input! Please enter a valid number that corresponds to an option on the menu.\n")

main()