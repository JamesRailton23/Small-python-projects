import random

# used to collect the hand the player will use and the hand the computer will use
player_hand = input("Rock, Paper or Scissors: ")
hand_choice = ("Rock","Paper","Scissors")
computer_hand = random.choice(hand_choice)

# if block for player hand as rock
if player_hand == "rock":
    if computer_hand == "Rock":
        print("Computer has rock: TIE")

    elif computer_hand == "Paper":
        print("Computer has paper: YOU LOSE!!")

    elif computer_hand == "Scissors":
        print("Computer has scissors: YOU WIN!!")

# elif block for player hand as paper
elif player_hand == "paper":
    if computer_hand == "Rock":
        print("Computer has rock: YOU WIN!!")

    elif computer_hand == "Paper":
        print("Computer has paper: TIE")

    elif computer_hand == "Scissors":
        print("Computer has scissors: YOU LOSE!!")

# if block for player hand as scissors
elif player_hand == "scissors":
    if computer_hand == "Rock":
        print("Computer has rock: YOU LOSE!!")

    elif computer_hand == "Paper":
        print("Computer has paper: YOU WIN!!")

    elif computer_hand == "Scissors":
        print("Computer has scissors: TIE!!")

# used to ensure that player has selected correct value
else:
    print("an error has occured: please try again")