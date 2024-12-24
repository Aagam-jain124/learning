
import random

def draw_hangman(attempts):
    stages = [
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        ''',
        '''
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        ''',
        '''
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        ''',
        '''
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        '''
    ]
    return stages[6 - attempts]

def hangman():
    words = ["python", "hangman", "game", "programming","lame", "computer"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word contains", len(secret_word), "letters.")

    while True:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("\nWord:", display_word)
        print("Attempts left:", attempts)
        print(draw_hangman(attempts))

        if display_word == secret_word:
            print("Congratulations! You guessed the word correctly:", secret_word)
            break

        if attempts == 0:
            print("Game over! The word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess!")

hangman()

