import random

number=random.randint(1,100)
attempt=0
print("Welcome! To The Number Guessing Game")
print("Guess a number from 1 to 100")
while True:
    guess=int(input("Enter the number: "))
    attempt+=1

    if guess>number:
        print("Too High")
    elif guess<number:
        print("Too low")
    else:
        print("Congrulation! You guess the correct number")
        print("Total attempts: ",attempt)
        break        