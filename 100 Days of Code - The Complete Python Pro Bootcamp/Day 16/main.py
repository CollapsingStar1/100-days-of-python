import coffee_maker, menu, money_machine

machine = coffee_maker.CoffeeMaker()
menu = menu.Menu()
money_machine = money_machine.MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if machine.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            machine.make_coffee(drink)

