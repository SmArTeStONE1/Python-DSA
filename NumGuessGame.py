import time
import random


print("-----WELCOME TO THE NUMBER GUESSING GAME-----")
time.sleep(2)
print()

print("Today the judges have picked a number from 1 to 20.")
time.sleep(2)
print("You will have a limited number of attempts to guess it.")
time.sleep(2)


while True:
    try:
        max_attempts = int(input("How many attempts would you like? "))
        if max_attempts <= 0:
            print("Please enter a positive number.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

print("Whoever guesses it first wins.")
time.sleep(1)
print("Good luck!")
time.sleep(1.5)

# Generate the random number
rannum = random.randint(1, 20)

# Game loop
for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"Guess {attempt}: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if guess == rannum:
        print("You Won!!! 🎉")
        break
    else:
        if guess < rannum:
            print("Too low!")
        else:
            print("Too high!")

        if attempt < max_attempts:
            print("Try Again...")
            time.sleep(1)
        else:
            print(f"You Lost! The correct number was: {rannum}")