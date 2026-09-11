import random
import os
import art
import game_data

data = game_data.data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_higher_lower():
    score = 0
    game_should_continue = True

    # Initial random pick for Option A
    option_a_index = random.randint(0, len(data) - 1)

    while game_should_continue:
        clear_screen()
        print(art.logo)

        if score > 0:
            print(f"You're right! Current score: {score}.\n")

        # Pick Option B and ensure it is never identical to Option A
        option_b_index = random.randint(0, len(data) - 1)
        while option_a_index == option_b_index:
            option_b_index = random.randint(0, len(data) - 1)

        account_a = data[option_a_index]
        account_b = data[option_b_index]

        # Display options
        print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}")
        print(art.vs)
        print(f"Against B: {account_b['name']}, {account_b['description']}, from {account_b['country']}")

        user_option = input("\nWho has more followers? Type 'A' or 'B': ").lower().strip()

        follower_count_a = account_a["follower_count"]
        follower_count_b = account_b["follower_count"]

        # Check guess
        is_correct = (
            (user_option == "a" and follower_count_a > follower_count_b) or
            (user_option == "b" and follower_count_b > follower_count_a)
        )

        if is_correct:
            score += 1
            # Option B becomes the next Option A
            option_a_index = option_b_index
        else:
            game_should_continue = False
            clear_screen()
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")

play_higher_lower()