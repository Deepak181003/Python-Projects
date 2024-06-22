import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
print("-------------------------------------------")
while True:
    # Ask the user to guess the number
    user_guess = int(input("Guess a number: "))
    print("-------------------------------------------")
    # Check if the user's guess is correct
    if user_guess == secret_number:
        print(" Congratulations! You guessed the correct number!")
        break

    # Provide hints if the user's guess is too high or too low
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
