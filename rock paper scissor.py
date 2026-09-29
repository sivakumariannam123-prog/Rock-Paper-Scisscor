import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter rock, paper, or scissors: ").lower()

if user not in choices:
    print("Invalid choice!")

elif user == computer:
    print("Computer:", computer)
    print("It's a tie!")

elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("Computer:", computer)
    print("You win!")

else:
    print("Computer:", computer)
    print("Computer wins!")