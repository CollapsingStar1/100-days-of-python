print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0

def logic(size, pepperoni, extra_cheese):
    global bill
    if size == "s":
        bill += 15
    if size == "m":
        bill += 20
    if size == "l":
        bill += 25
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1
    return bill



logic(size, pepperoni, extra_cheese)
print(f"Your final bill is: ${bill}.")

