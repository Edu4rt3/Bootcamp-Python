# Hangman
import random
word_list = ["apple", "banana", "computer", "dolphin", "elephant","fantastic", "giraffe", "happiness", "internet", "jungle","kangaroo", "lighthouse", "mountain", "notebook", "ocean","penguin", "question", "rainbow", "sunshine", "tiger"]

word = random.choice(word_list)
word_len = len(word)
placeholder = ""
for position in range(word_len):
    placeholder += "_"
print(placeholder)

life = 6
game_over = False
correct_letters = []

while not game_over:
        
    guess = input("Choose a letter \n").lower()
    display = ""
    if guess in correct_letters:
        print(f"You already guessed {guess}")
    for letter in word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in word:
        life -= 1
        print(f"You have {life} lives now")
        if life == 0:
            game_over = True
            print("Good luck next time!")
    if "_" not in display:
        game_over = True
        print("Congrats you win the game!!")