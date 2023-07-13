from data import MENU, resources


def calc_money(q, d, n, p):
    user_money = q*0.25 + d*0.10 + n*0.05 + p*0.01
    return user_money


def coffee_total(coffee_choice):
    if coffee_choice == "espresso":
        return MENU[coffee_choice]["cost"]
    elif coffee_choice == "latte":
        return MENU[coffee_choice]["cost"]
    elif coffee_choice == "cappuccino":
        return MENU[coffee_choice]["cost"]


def machine():
    machine_is_on = True

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0

    while machine_is_on:

        coffee_choice = input("What would you like? (espresso/latte/cappuccino):")

        if coffee_choice == "report":
            print(f"Water: {water}")
            print(f"Milk: {milk}")
            print(f"Coffee: {coffee}")
            print(f"Money: {money}")

        elif coffee_choice == "off":
            print("GoodBye!")
            machine_is_on = False

        elif water < MENU[coffee_choice]["ingredients"]["water"]:
            print("Sorry, there's not enough water")
        elif milk < MENU[coffee_choice]["ingredients"]["milk"]:
            print("Sorry, there's not enough milk")
        elif milk < MENU[coffee_choice]["ingredients"]["coffee"]:
            print("Sorry, there's not enough coffee powder")
        else:
            print("Please insert coins.")
            quarter = int(input("How many quarters? "))
            dime = int(input("How many dimes? "))
            nickel = int(input("How many nickels? "))
            penny = int(input("How many pennies? "))

            if calc_money(quarter, dime, nickel, penny) < coffee_total(coffee_choice):
                print("Sorry that's not enough money. Money refunded")

            else:
                change = calc_money(quarter, dime, nickel, penny) - coffee_total(coffee_choice)
                print(f"Here is ${change} in change")
                print(f"Here is your {coffee_choice}. Enjoy!")
                water -= MENU[coffee_choice]["ingredients"]["water"]
                milk -= MENU[coffee_choice]["ingredients"]["milk"]
                coffee -= MENU[coffee_choice]["ingredients"]["coffee"]
                money += MENU[coffee_choice]["cost"]


machine()
