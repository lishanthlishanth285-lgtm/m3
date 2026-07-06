import random
while True:
    user_action = input("Enter your action (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"user action: {user_action}, computer action: {computer_action}")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock" and computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    elif user_action == "paper" and computer_action == "rock":
        print("Paper covers rock! You win!")
    elif user_action == "scissors" and computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("You lose!")
