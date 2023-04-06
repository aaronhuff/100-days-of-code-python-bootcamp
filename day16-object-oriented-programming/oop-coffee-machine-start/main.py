from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

banner = """
1. Print supply report
2. Print profit report
3. Make drink
4. Shutoff machine
"""

while True:
    print(banner)
    user_action = input("Option: ")
    match int(user_action):
        case 1:
            coffee_maker.report()
        case 2:
            money_machine.report()
        case 3:
            drinks = menu.get_items()
            print('Drinks:')
            for item in drinks:
                print(f'- {item}')
            drink_option = input("Drink: ")
            drink = menu.find_drink(drink_option)
            if coffee_maker.is_resource_sufficient(drink):
                print(f'{drink.name} costs {drink.cost}.')
                payment = money_machine.make_payment(drink.cost)
                if payment:
                    coffee_maker.make_coffee(drink)
            else:
                print('Not enough resources available')
        case 4:
            money_machine.report()
            coffee_maker.report()
            exit()
