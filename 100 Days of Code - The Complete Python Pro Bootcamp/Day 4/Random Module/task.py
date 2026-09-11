import random
ran_num = random.randint(1, 10)
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
print(random.choice(cards))

for items in cards:
    print(random.choice(cards), end=" ")