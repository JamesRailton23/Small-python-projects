import sys

def game():
    points = 0
    questions_and_answer = {"Which of these planes are for regional routes": "A",
                            "What is the airport code for heathrow": "D",
                            "Who made the B747": "C",
                            "Which of these companies not longer produce commercial planes": "D"}

    choice = [['A = A220', 'B = 747', 'C = AN225', 'D = A380'],
    ['A = EGKK', 'B = EGPH', 'C = KJFK', 'D = EGLL '],
    ['A = AIRBUS', 'B = MIG', 'C = BOEING', 'D = BAE'],
    ['A = AIRBUS', 'B = MIG', 'C = BOEING', 'D = BAE']]

    play_number = 0
    for i in questions_and_answer:
        print(i)
        for j in choice[play_number]:
            print(j)

        guess = input()
        if guess == questions_and_answer.get(i):
            points += 1
        play_number += 1
    print("Your scored {score} out of 4".format(score=points))

start = input("Do you want to start the game, Y = Yes, anything else ")
if start == "Y" or start == "y":
    play = "Y"
    while play == "Y" or play == "y":
        print()
        game()
        play = input("Do you want to play the game, Y = Yes, anything else ")
else:
    sys.exit()
