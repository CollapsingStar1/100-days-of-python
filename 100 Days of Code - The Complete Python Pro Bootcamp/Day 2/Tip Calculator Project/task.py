print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage_tip = (tip + 100) / 100
total_bill = bill * percentage_tip
cost_each = round(total_bill / people,1)
print(cost_each)

