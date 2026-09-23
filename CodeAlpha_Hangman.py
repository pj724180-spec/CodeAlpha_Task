import random

word_list = ["apple", "beautiful", "potato"]

lives = 6
chosen_word = random.choice(word_list)

print(chosen_word)

display = []

for i in range(len(chosen_word)):
    display += "_"

print(display)

game_over = False

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    for position, letter in enumerate(chosen_word):
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)

    if guessed_letter not in chosen_word:
        lives -= 1
        print("Wrong guess! Lives left:", lives)

        if lives == 0:
            game_over = True
            print("You Lose!!")
            print("The word was:", chosen_word)

    if "_" not in display:
        game_over = True
        print("You Win!!")