import main

menu = main.MENU
resource = main.resources

profit = 0.0  # 1. Track total earnings


def greet():
    return input("\nWhat would you like to drink? (espresso/latte/cappuccino): ").lower().strip()


def pay():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters, dimes, nickles, pennies


def is_drink_available(ingredient_list):
    for item, amount in ingredient_list.items():
        if amount > resource[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_transaction(cost_drink, quarters, dimes, nickles, pennies):
    global profit
    total_pay = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total_pay >= cost_drink:
        profit += cost_drink  # 2. Add cost to machine earnings
        change = round(total_pay - cost_drink, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, ingredient_list):
    for item, amount in ingredient_list.items():
        resource[item] -= amount
    print(f"Here is your drink, {drink_name}. Enjoy!")


def coffee_machine():
    print("Hello, welcome to the coffee machine!")  # Printed once before the loop
    is_on = True
    while is_on:
        choice = greet()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resource['water']}ml")
            print(f"Milk: {resource['milk']}ml")
            print(f"Coffee: {resource['coffee']}g")
            print(f"Money: ${profit:.2f}")  # 3. Displayed in report
        elif choice in menu:
            drink = menu[choice]
            if is_drink_available(drink["ingredients"]):
                quarters, dimes, nickles, pennies = pay()
                if process_transaction(drink["cost"], quarters, dimes, nickles, pennies):
                    make_drink(choice, drink["ingredients"])
        else:
            print("I'm sorry, I didn't understand that command.")


coffee_machine()