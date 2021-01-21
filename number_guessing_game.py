# Number guessing game

# Importing random module
import random

# Generating a random number and store it in a variable "n"
n = random.randint(1,10)

# Getting input from user
guess = int(input("Enter a number from 1 to 10: "))

# Making  a while loop to ask input multiple times
while True: 

    # printing your guess is low when guess is lower than n
    if guess < n:
        print("Your Guess is low")
        # and asking input again
        guess = int(input("Try again: "))

    # printing your guess is High when guess is higher than n
    elif guess > n:
        print("Your Guess is High")
        # and asking input again
        guess = int(input("Try again: "))

    # Print the guess is correct when user guessed correctly
    else:
        print("Your guess is correct")
        #stoping program after running this program
        break
