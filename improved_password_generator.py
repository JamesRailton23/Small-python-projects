import random

password_length = int(input("Enter Password Length: "))
password = ""

characters = ["a", "b", "c", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]

upper_characters = ["A", "B", "C", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

special_characters = ["!", "£", "$", "%", "*", "(", ")", "{", "}", "#", "/", "`", "?"]

for i in range(password_length):
    selector = random.randint(1, 4)
    if selector == 1:
        password += random.choice(characters)
    elif selector == 2:
        password += random.choice(upper_characters)
    elif selector == 3:
        password += random.choice(numbers)
    elif selector == 4:
        password += random.choice(special_characters)


else:
    print("Your password is:", password)
