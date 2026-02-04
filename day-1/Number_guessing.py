import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter Your Guess: "))
    attempts += 1

    if guess > number:
        print("Too High!")
    elif guess < number:
        print("Too Low!")
    else:
        print("Congratulations! You guessed the correct number.")
        print("Total attempts:", attempts)
        break
