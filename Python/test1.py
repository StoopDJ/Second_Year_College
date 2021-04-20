# Function: Write a Python program that will prompt the user for a number, and print all the Kaprekar numbers
# from 10 to that number.
# Use functions where appropriate to structure your code.

# Code by : Amir Akbari
# Compiler used: PyCharm

def Kap():
    users_input = input("Enter a max limit (Inclusive):\n")
    users_input = int(users_input)  # making the variable an int
    print("The list of all Kaprikar numbers from ", 10, "to", users_input, "is: \n")

    for i in range(10, users_input + 1):
        # Get the digits from the square in a list:
        sqr = i ** 2
        digits = str(sqr)

        # Now loop from 1 to length of the number - 1, sum both sides and check
        length = len(digits)
        for x in range(1, length):
            left = int("".join(digits[:x]))
            right = int("".join(digits[x:]))
            if (left + right) == i:
                print(" " + str(i))

def Kap_checker():
    num_checker = input("Enter the number that you would like to check:\n")
    num_checker = int(num_checker)

    for i in range(num_checker, num_checker + 1):
        # Get the digits from the square in a list:
        sqr = i ** 2
        digits = str(sqr)

        # Now loop from 1 to length of the number - 1, sum both sides and check
        length = len(digits)
        for x in range(1, length):
            left = int("".join(digits[:x]))
            right = int("".join(digits[x:]))
            if (left + right) == num_checker:
                print(num_checker, "is a Kaprekar number because when you square it you get", sqr)
                print("This can be split into", left, "and", right, "which then adds up to", num_checker)
            elif (left + right) != num_checker:
                print(num_checker, "is not a Kaprekar number")
                break  # leave the loop

# Main function

# Menu to choice which function you want
print("1. Check if a number is a Kaprekar number\n")
print("2. See the list of Kaprekar numbers within a specified range\n")
choice = input("Please enter the number that corresponds to what option you want:\n")
choice = int(choice)  # making the variable an int

if choice == 1:
    # Call function
    Kap()

elif choice == 2:
    Kap_checker()

else:
    print("Invalid input\n")
