
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Guess the number between 1 and 100!")

    while True:
        guess = input("Enter your guess or type 'end' to quit: ")

        if guess.lower() == "end":
            print("Game ended!")
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

guessing_game()
