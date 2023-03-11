# Random Password Creator Using Tuples, and the Random Module in Python to Generate Passwords

from random import *  # used to get modul for random number generation

password_letters = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z")  # tuple used to store the letters of the alphabet

password_characters = (
    "!", "£", "$", "%", "^", "&", "*", ";", ";", "@", "?", "<", ">", "#", "~", "+", "=", "-", "_", "[", "]", "|", "`",
    "¬")  # tuple used to store the special characters

password_numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")  # tuple used to store the numbers


def password_generator():
    # generates 3 random letters
    password_1_let = password_letters[randrange(0, len(password_letters))]
    password_2_let = password_letters[randrange(0, len(password_letters))]
    password_3_let = password_letters[randrange(0, len(password_letters))]

    # generates 3 random special characters
    password_4_chr = password_characters[randrange(0, len(password_characters))]
    password_5_chr = password_characters[randrange(0, len(password_characters))]
    password_6_chr = password_characters[randrange(0, len(password_characters))]

    # generates 4 random numbers
    password_7_int = password_numbers[randrange(0, len(password_numbers))]
    password_8_int = password_numbers[randrange(0, len(password_numbers))]
    password_9_int = password_numbers[randrange(0, len(password_numbers))]
    password_10_int = password_numbers[randrange(0, len(password_numbers))]

    # combines the letters, special characters and numbers
    # it also creates a lower case and uppercase version of the letters
    final_lower_letter = password_1_let + password_2_let + password_3_let
    final_upper_letter = password_1_let.upper() + password_2_let.upper() + password_3_let.upper()
    final_char = password_4_chr + password_5_chr + password_6_chr
    final_int = password_7_int + password_8_int + password_9_int + password_10_int

    # shuffles password
    un_shuffled_password = final_lower_letter + final_char + final_int + final_upper_letter
    final_password = ''.join(sample(un_shuffled_password, len(un_shuffled_password)))

    # returns the shuffled random 10 character password
    return final_password


def user_action():
    # used to determine if the user wants a password via ternary statement
    wants_password = input("Would you like a random 10 digit password? Type Yes or No - ")
    print("your password is -", password_generator()) if wants_password == "yes" or wants_password == "YES" \
        else user_action()

    # restarts the method
    print()
    user_action()


user_action()  # invokes the random password generator
