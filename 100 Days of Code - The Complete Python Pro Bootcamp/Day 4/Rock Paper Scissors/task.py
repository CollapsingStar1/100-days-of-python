import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n>>> ")

# 1. Validate user input first
if not user_input.isdigit() or int(user_input) not in [0, 1, 2]:
    print("You typed an invalid number. You lose!")
else:
    user_choice = int(user_input)
    computer_choice = random.randint(0, 2)

    # 2. Display choices with ASCII art
    print("\nYou chose:")
    print(game_images[user_choice])

    print("Computer chose:")
    print(game_images[computer_choice])

    # 3. Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")