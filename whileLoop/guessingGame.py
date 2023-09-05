# Write a Python program for a simple "Guess the Number" game. In this game, the computer selects a random number between 1 and 100 (inclusive), and the player has to guess that number. The player is given multiple chances to guess the number, and after each guess, the computer provides feedback on whether the guess is too high, too low, or correct. The game continues until the player guesses the correct number or runs out of chances.

# Here are the rules and requirements:

# The computer generates a random number between 1 and 100 at the start of the game.
# The player is given a maximum of 10 chances to guess the number.
# After each guess, the computer should provide one of the following messages:
# "Too high! Try again."
# "Too low! Try again."
# "Congratulations! You've guessed the number." (if the guess is correct).
# "Sorry, you've run out of chances. The correct number was [the correct number]." (if the player runs out of chances).
# The program should ask the player for their guess using a while loop until the player guesses the correct number or runs out of chances.
# After the game is over (either the player guessed correctly or ran out of chances), ask the player if they want to play again.
# You can use Python's random module to generate random numbers.

# Hint: You can use a variable to keep track of the number of remaining chances and update it in each iteration of the loop.

import random;

random_number = random.randint(1,100)

print(random_number)