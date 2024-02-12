import random

user = input("Enter a choice (rock, paper, scissors): ")
computer=random.choice(["rock", "paper", "scissors"])


if user == computer:
  print("Its a tie!")
elif computer == "rock" and user == "scissors":
  print("Computer wins!")
elif computer == "paper" and user == "rock":
  print("Computer wins!")
elif computer == "scissors" and user == "paper":
  print("Computer wins!")
else:
  print("You win!!!")
