from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
coffee_menu = Menu()


is_on = True


while is_on:
    options = coffee_menu.get_items()
    client_choice = input(f'What would you like to drink? ({options}): ')
    if client_choice == 'off':
        is_on = False
    elif client_choice == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(client_choice)
        if coffee_machine.is_resource_sufficient(drink):
            payment = money_machine.make_payment(drink.cost)
            if payment is True:
                coffee_machine.make_coffee(drink)
