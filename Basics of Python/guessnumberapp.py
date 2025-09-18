import random
number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess != number:
    guess = int(input("Wrong guess! Try again: "))
    print("Computer Guessed ", number)
print("Correct Guess!")

#while loop can be used to allow multiple attempts until the correct guess
