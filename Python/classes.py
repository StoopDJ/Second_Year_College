# Function: To write classes
# Classes
class Rectangle:

    def __init__(self, length, width):  # Initialise the variables.
        self.length = length
        self.width = width

    def __sides__(self):  # Send the data back to the main function.
        return self.length, self.width

class AIB:

    def __init__(self, first, last, accnum, address):
        self.first = first
        self.last = last
        self.accnum = accnum
        self.address = address

    def __info__(self):
        return self.first, self.last, self.accnum, self.address

class Clock:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __hms__(self):
        return self.hours, self.minutes, self.seconds

# Functions
def rec():
    shape = Rectangle(10, 20)
    print("\nThe length of the rectangle is", shape.length, "and the width is", shape.width, ".")

def bank():
    bank = AIB("Amir", "AK", "1234567", "Non of ur business")
    print("\nName: ", bank.first, bank.last)
    print("Account Number: ", bank.accnum)
    print("Address: ", bank.address)

def time():
    time = Clock("15", "04", "00")
    print(time.hours, ":", time.minutes, ":", time.seconds)


# Main function
# Menu to choice which function you want
print("1. Rectangle class.\n")
print("2. Bank class.\n")
print("3. Clock class\n")

while 1:
    choice = input("\nPlease enter the number that corresponds to what option you want:\n")
    choice = int(choice)  # making the variable an int

    if choice == 1:
        # Call function
        rec()

    elif choice == 2:
        bank()

    elif choice == 3:
        time()

    else:
        print("Invalid input\n")