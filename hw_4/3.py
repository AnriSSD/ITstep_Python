import random

target_number = random.randint(1, 100)
user_guess = None

while user_guess != target_number:
    user_guess = int(input("Guess the number: "))
    if user_guess < target_number:
        print("Too low, try again!")
    elif user_guess > target_number:
        print("Too high, try again!")

print("Congratulations! You guessed the correct number.")
