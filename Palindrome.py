"""
File: a7.py

"""

from stack import Stack


def isPalindrome(sentence):
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack()  # Creates a stack called stk.

    # *** Write your code here ***
    string = sentence  # Variable to hold the user input string

    special_ch = '!@#$%^&*(),.?;:''" """<>/[]{}|+=_-`|'  # List of characters that are meant to be
    # removed from string if seen

    new_string = ""  # empty string to hold edited string from the user input.
    for ch in string:  # for loop to search string.
        if ch not in special_ch:  # if the character doesn't match the special character then add it to the new string.
            new_string = new_string + ch  # adds the ch to the new string in each iteration.

    for character in new_string:  # for loop to search new_string
        stk.push(character)  # pushes the stack taking the characters from the string.

    reverse_text = ""  # Meant to hold the reverse string
    while not stk.isEmpty():  # while loop meant to check while it is not empty.
        reverse_text = reverse_text + stk.pop()  # Adds the pop to the reverse string.

    if new_string == reverse_text:  # if checks to see if new_string is equal to the reverse string.
        return True  # returns true if above is true.
    else:
        return False  # returns false if above condition is false.


# *** Do not modify main() ***
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")


main()
