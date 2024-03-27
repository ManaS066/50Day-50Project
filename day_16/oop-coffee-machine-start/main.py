from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
cofee_maker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f'what would you like ? {option}:')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        money.report()
        cofee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if cofee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                cofee_maker.make_coffee(drink)
