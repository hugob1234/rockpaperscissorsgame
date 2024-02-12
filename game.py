import random

while True:
  user = input("Enter a choice (rock, paper, scissors, end): ")
  computer=random.choice(["rock", "paper", "scissors"])


  if user == computer:
    print("Its a tie!")
  elif computer == "rock" and user == "scissors":
    print("Computer wins!")
  elif computer == "paper" and user == "rock":
    print("Computer wins!")
  elif computer == "scissors" and user == "paper":
    print("Computer wins!")
  elif user == "end":
    print("See you later :)")
    break
  else:
    print("You win!!!")

