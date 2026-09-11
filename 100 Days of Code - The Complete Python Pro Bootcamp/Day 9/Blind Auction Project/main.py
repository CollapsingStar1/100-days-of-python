# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
print("Welcome to the Auction")
user_nr = int(input("How many people are going to bid? "))

user_dict = {}

for i in range(user_nr):
    name = input("What is your name? ")
    price = float(input("What is your bid? "))
    user_dict[name] = price
    print("\n" * 50)

print(user_dict)

def highest_bidder(user_dict):
    highest_bid = 0
    winner = ""
    for bidder, amount in user_dict.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    return winner


winner = highest_bidder(user_dict)
print("The highest bidder is: ", winner, " with a bid of: ", user_dict[winner], "$")

