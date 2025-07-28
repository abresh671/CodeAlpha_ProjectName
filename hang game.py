import random

def hangman():
    """
    A simple text-based Hangman game.
    """
    words = ["python", "hangman", "coding", "program", "challenge"]
    chosen_word = random.choice(words).lower()
    guessed_letters = []  # This list stores all guessed letters
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        if "_" not in display_word:
            print(f"\nCongratulations! You've guessed the word: {chosen_word}")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.append(guess)  # Corrected from guessed_guesses to guessed_letters
            incorrect_guesses += 1

    else:
        print("\nGame Over! You ran out of guesses.")
        print(f"The word was: {chosen_word}")

# Run the game
if __name__ == "__main__":
    hangman()