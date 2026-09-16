# Number guessing game
import random

com = random.randint(1, 100)
tries = 0

while True:
    tries += 1
    user_guess = int(input("Enter your guess: "))

    if user_guess == com:
        print(f"Congratulations! You guessed the number in {tries} tries.")
        break
    elif user_guess < com:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

#Rock, Paper, Scissors game
import random

choices = ["rock", "paper", "scissors"]
tries = 0
while True:
    tries += 1
    com = random.choice(choices)
    user_guess = input("Enter your choice (rock, paper, scissors): ")

    if user_guess == com:
        print(f"It's a draw! You made a guess in {tries} tries.")
    elif (user_guess == "rock" and com == "scissors") or (user_guess == "scissors" and com == "paper") or (user_guess == "paper" and com == "rock"):
        print(f"You win! You made a guess in {tries} tries.")
        break
    else:
        print("You lose!")