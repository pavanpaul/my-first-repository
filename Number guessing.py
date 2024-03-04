import random

def number_guessing_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    random_number = random.randint(lower_bound, upper_bound)

    # Initialize the number of guesses
    guesses = 0

    print(f"Guess a number between {lower_bound} and {upper_bound}")

    while True:
        # Get user input
        user_guess = input("Enter your guess: ")

        # Check if the input is a valid integer
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue

        # Convert user input to an integer
        user_guess = int(user_guess)
        guesses += 1

        # Check if the guess is correct
        if user_guess == random_number:
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            break
        elif user_guess < random_number:
            print("Try guessing higher.")
        else:
            print("Try guessing lower.")

# Run the game
number_guessing_game()
