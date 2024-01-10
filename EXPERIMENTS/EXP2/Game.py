import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    print(secret_number)
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it.")

    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")
            break  # Exit the loop

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        guessing_game()
    else:
        print("Thank you for playing!")

# Start the game
guessing_game()
