import random

player_score = 0
computer_score = 0

print("-----------------------------")
print("Rock! Paper! Scissors! Shoot!")
print("-----------------------------")

print("1) Rock (✊)")
print("2) Paper (✋)")
print("3) Scissors (✌️)")
player_choice = int(input("What is your choice?: "))
computer_choice = random.randint(1, 3)

print(f"You chose: {player_choice}")
print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == 1 and computer_choice == 3) or \
     (player_choice == 2 and computer_choice == 1) or \
     (player_choice == 3 and computer_choice == 2):
    print("You win!")
else:
    print("You lose!")
