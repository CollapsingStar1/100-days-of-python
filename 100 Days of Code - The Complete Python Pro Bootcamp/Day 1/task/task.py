import random

print("Hello new comer, to the great world of Dragama")
city_user = input("What is your favorite city?\n")
pet_user = input("What is your favorite pet?\n")

# Combine all letters and remove spaces
letters = list((city_user + pet_user).replace(" ", ""))

# Shuffle the characters
random.shuffle(letters)

# Join them back into a single string
shuffled_name = "".join(letters).capitalize()

print(f"Your generated name is: {shuffled_name}")