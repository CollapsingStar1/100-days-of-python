import random

list_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# Both player and computer start with 2 cards
your_pick = [random.choice(list_cards), random.choice(list_cards)]
computer_pick = [random.choice(list_cards), random.choice(list_cards)]


def sum_cards(cards):
    return sum(cards)


def computer_logic(computer_pick):
    # 'while' ensures the dealer keeps drawing until reaching at least 17
    while sum_cards(computer_pick) < 17:
        computer_pick.append(random.choice(list_cards))
    return computer_pick


def play_game(your_pick, computer_pick):
    game_over = False

    # 1. PLAYER'S TURN LOOP
    while not game_over:
        player_score = sum_cards(your_pick)
        print(f"Your cards: {your_pick}, current score: {player_score}")
        print(f"Computer's first card: {computer_pick[0]}")

        # Check if player already busted
        if player_score > 21:
            print("You went over 21. You bust! You lose. 💥")
            return

        choice = input("Type 'hit' to get another card, or 'stand' to pass: ").lower().strip()

        if choice == "hit":
            your_pick.append(random.choice(list_cards))
        elif choice == "stand":
            game_over = True

    # 2. COMPUTER'S TURN (Hits until 17 or higher)
    computer_logic(computer_pick)

    player_final = sum_cards(your_pick)
    computer_final = sum_cards(computer_pick)

    print("\n" + "=" * 30)
    print(f"Your final hand: {your_pick}, final score: {player_final}")
    print(f"Computer's final hand: {computer_pick}, final score: {computer_final}")
    print("=" * 30)

    # 3. COMPARE FINAL SCORES
    if player_final > 21:
        print("You bust! You lose. 😭")
    elif computer_final > 21:
        print("Computer went over 21! You win! 🏆")
    elif player_final > computer_final:
        print("You win! 🏆")
    elif player_final < computer_final:
        print("You lose. 😭")
    else:
        print("It's a draw! 🤝")


play_game(your_pick, computer_pick)