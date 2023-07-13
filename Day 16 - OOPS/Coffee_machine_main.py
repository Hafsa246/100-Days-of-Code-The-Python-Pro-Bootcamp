from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
coffee_maker_machine = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:

    options = menu.get_items()
    order_name = input(f"What drink would you like? {options}")

    if order_name == "report":
        my_money_machine.report()
        coffee_maker_machine.report()
    elif order_name == "off":
        is_on = False
    else:
        drink = menu.find_drink(order_name)
        if coffee_maker_machine.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
                coffee_maker_machine.make_coffee(drink)