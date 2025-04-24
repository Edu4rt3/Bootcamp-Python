# Number guessing game
import random

print("Welcome to the Number guessing game!\n I'm thinking of a number between 1 and 100.")

tries = 0
number = random.randint(1, 101)
guess = 0
guessed_numbers = []
should_continue = True


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    tries = 10
elif difficulty == "hard":
    tries = 5
else:
    print("You have typed something wrong!")
    should_continue = False

def compare(number, guess):
    if guess in guessed_numbers:
        print("You alrealdy guessed this number!")
    elif number > guess:
        print("Too low\n Guess again")
        global tries
        tries -= 1
    elif number < guess:
        print("Too high\n Guess again")
        tries -= 1
    else:
        print("You guessed it right!!")
        global should_continue
        should_continue = False

while should_continue == True:
    print(f"You have {tries} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    compare(number, guess)
    guessed_numbers.append(guess)
    if tries == 0:
        should_continue = False
        print("Sorry your attempts has ended, good luck next time!")
    