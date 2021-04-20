# Converting binary to decimal and vice versa

end = 0
user_str = 1
user_int = 1

def dec2bin():
        # This converts the users decimal input into binary and displays it

        end = 0
        while end == 0:
            user_str = input("Please enter any integer or enter 'exit' to return to the menu: ")
            # prompt the user for an input

            if user_str < '0':
                print("Error, Please only enter positive whole numbers\n")
            elif user_str == '0':
                print("Your input in binary is: 0\n")
            elif user_str == 'exit':
                print("Loading...\n")
                end = 1
            else:
                user_int = int(user_str)  # change the input into an integer
                user_int = bin(user_int)[2:]

                print("Your input in binary is:", user_int, "\n")
        return

def bin2dec():
        " This converts binary values back into decimal"

        end = 0
        while end == 0:
            user_str = input("Please enter any binary string or enter 'exit' to return to the menu: ")
            # prompt the user for an input

            if user_str < '':
                print("Error, Please only enter binary strings only\n")
            elif user_str == '0':
                print("Your input in decimal is: 0\n")
            elif user_str == 'exit':
                print("Loading...\n")
                end = 1
            else:
                user_str = int(user_str, 2)
                print("Your input in decimal is ", user_str, "\n")
        return


while end == 0:
        print("Please enter the number that corresponds to the option you would like\n")
        selection = input("1. Convert decimal to binary.\n2. Convert binary to decimal.\n3. Terminate the program.\n\n")

        if selection == '1':
                dec2bin()
        elif selection == '2':
                bin2dec()
        elif selection =='3':
                print("Thank you")
                end = 1






