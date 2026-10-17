
import random

# Predefined list of words
words = [
    "PYTHON",
    "HANGMAN",
    "COMPUTER",
    "PROGRAMMING",
    "DEVELOPER",
    "KEYBOARD",
    "SCIENCE",
    "ARTIFICIAL"
]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = set()

# Maximum incorrect attempts
max_attempts = 6
remaining_attempts = max_attempts

print("=" * 35)
print("       WELCOME TO HANGMAN!")
print("=" * 35)
print("Guess the word one letter at a time.")
print(f"You have {max_attempts} incorrect attempts.\n")

# Main game loop
while remaining_attempts > 0:

    # Display guessed and hidden letters
    masked_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            masked_word += letter + " "
        else:
            masked_word += "_ "

    print("Word:", masked_word.strip())
    print("Guessed letters:", sorted(guessed_letters))
    print("Remaining attempts:", remaining_attempts)

    # Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word!")
        break

    # Get player's guess
    guess = input("\nEnter a single letter: ").strip().upper()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter. Try another.\n")
        continue

    guessed_letters.add(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!\n")
    else:
        remaining_attempts -= 1
        print("Wrong guess! Try again.\n")

else:
    print("You ran out of attempts!")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")
