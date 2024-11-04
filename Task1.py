# TASK 1 : HANGMAN GAME...

import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "openai"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        "------\n|    |\n|    O\n|   /|\\\n|   / \\\n|",
        "------\n|    |\n|    O\n|   /|\\\n|   /",
        "------\n|    |\n|    O\n|   /|\\",
        "------\n|    |\n|    O\n|   /|",
        "------\n|    |\n|    O",
        "------\n|    |\n|",
        "------\n|",
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
            print("Good guess!")
        else:
            tries -= 1
            guessed_letters.append(guess)
            print(f"{guess} is not in the word.")

        print(display_hangman(tries))
        print(word_completion)

        if "_" not in word_completion:
            guessed = True

    if guessed:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you've run out of tries. The word was '{word}'.")

play_hangman()
