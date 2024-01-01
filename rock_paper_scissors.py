import random
 
user_actions = input("Enter your actions: ")
Computer_obects = ['rock', 'scissors', 'paper']
opponent_actions = random.choice(Computer_obects)
print(f"\nYou choice is {user_actions}. Your opponent choice is {opponent_actions}.")
 
if user_actions == opponent_actions:
    print(f"\nBoth players selected {user_actions}. It's a tie!")
elif user_actions == "rock":
    if opponent_actions == "scissors":
        print(f"\nYou win!")
elif user_actions == "scissors":
    if opponent_actions == "paper":
        print(f"\nYou win!")
elif user_actions == "paper":
    if opponent_actions == "rock":
        print(f"\nYou win!")
elif user_actions == "scissors":
    if opponent_actions == "rock":
        print(f"\nYou lose! Computer win!")
elif user_actions == "paper":
    if opponent_actions == "scissors":
        print(f"\nYou lose! Computer win!")
elif user_actions == "rock":
    if opponent_actions == "paper":
        print(f"\nYou lose! Computer win!")
