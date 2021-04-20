# Create a program that checks if a string is a palindrome i.e. reads the same backwards
# The program should be able to deal with punctuation and capital letters

import string

# function to check string is palindrome or not
def isPalindrome(user_word):
    # Using predefined function to
    # reverse to string print(s)
    user_word = user_word.lower() # removes any capital letters from the string

    bad_char = string.whitespace + string.punctuation # combination of white spaces and punctuation

    for i in bad_char:
        user_word = user_word.replace(i, "") # loop to check for and replace all bad characters with nothing

    rev = ''.join(reversed(user_word)) #reverses the word

    # Checking if both string are equal or not
    if (user_word == rev):
        return True
    return False

while(True):
    # main function
    user_word = input("Enter a word\n")
    ans = isPalindrome(user_word)

    if (ans):
        print("This is a palindrome")
    else:
        print("This is not a palindrome")