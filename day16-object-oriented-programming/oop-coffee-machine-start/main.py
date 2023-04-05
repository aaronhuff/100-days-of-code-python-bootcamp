from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

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
            my_coffee_maker.report()
        case 2:
            my_money_machine.report()
        case 3:
            x = 1
            for item in my_menu.get_items().split('/')[:-1]:
                print(f'{x}. {item}')
                x += 1
            drink_option = input("Option:")
            drink_name = my_menu.get_items().split('/')[int(drink_option)-1]
            drink = my_menu.find_drink(drink_name)
            if my_coffee_maker.is_resource_sufficient(drink):
                print(f'{drink.name} costs {drink.cost}.')
                payment = my_money_machine.make_payment(drink.cost)
                if payment:
                    my_coffee_maker.make_coffee(drink)
            else:
                print('Not enough resources available')
        case 4:
            my_money_machine.report()
            exit()
