# Write a Python program for a simple "Guess the Number" game. In this game, the computer selects a random number
# between 1 and 100 (inclusive), and the player has to guess that number. The player is given multiple chances to
# guess the number, and after each guess, the computer provides feedback on whether the guess is too high, too low,
# or correct. The game continues until the player guesses the correct number or runs out of chances.

# Here are the rules and requirements:

# The computer gener

import random

def guess_game():
    random_number = random.randint(1, 100)
    chances = 10
    while chances > 0:
        user_input = int(input("Type your number here: "))
        if user_input > random_number:
            print("Your number is too high, try again")
        elif user_input < random_number:
            print("Your number is too low, try again.")
        elif user_input == random_number:
            print("Congratulations! You have guessed the number!")
            break
        chances -= 1
        print("You have", chances, "chances left.")
    if chances == 0:
        print("Oops, you have run out of chances, try again!")

guess_game()
