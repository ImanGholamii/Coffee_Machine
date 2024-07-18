MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}


def get_order():
    """Receives order input and returns it"""
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return order


def say_enjoy(order):
    print(f"Here is your {order} ☕. Enjoy!")


def do_off():
    print(f"🔌        Turning off the coffee machine...      🔌")
    return True


def show_resources():
    """Show amount of remained resources."""
    return (f"Water: {resources['water']} ml\nMilk: {resources['milk']}ml"
            f"\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")


def process_order(order):
    """Receives order and processes it that it's an order or other commands"""
    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        return order
    elif order == 'report':
        print(show_resources())
        return 'report'
    elif order == 'off':
        do_off()
        return 'off'
    else:
        print("⚫ Wrong Input!")
        return 'wrong'


def resource_shortage_reporter(order, order_item, customer_payment):
    print(f"Sorry we can't make {order}.\n🛑Out of {order_item}\n"
          f"💲>>> Please take Your money.⬇️\n💲>>> ${format(customer_payment, '.2f')}")


def check_resources(order, resources, customer_payment):
    for item in MENU[order]['ingredients']:
        if resources[item] >= MENU[order]['ingredients'][item]:
            resources[item] -= MENU[order]['ingredients'][item]
            resources['money'] += MENU[order]['cost']

        else:
            resource_shortage_reporter(order=order, customer_payment=customer_payment, order_item=item)
            return False
    return True


# Payment

def get_coins():
    """get coins and saves in dictionary"""
    coins = {'pennies': int(input(f"🪙 Please insert Coins:➡️➡️➡️\n|__ How many pennies? ")),
             'nickles': int(input(f"\n|__ How many nickles? ")), 'dimes': int(input(f"\n|__ How many dimes? ")),
             'quarters': int(input(f"\n|__ How many quarters? "))}
    return coins


def process_coins(coins):
    """Calculate the monetary value of the coins inserted."""
    total = coins['pennies'] * 0.01 + coins['nickles'] * 0.05 + coins['dimes'] * 0.10 + coins['quarters'] * 0.25
    return total


def failed_transaction(coins):
    """Reports failed transaction. and back coins."""
    print(f"⚫ Not Sufficient Coins ❗\nPlease take your money.⬇️⬇️⬇️\n💲>>> ${format(coins, '.2f')}")
    return coins


def prepare_order(payment, order, resources):
    """back coins to customer if it's not sufficient and reload resources else prepare Order."""
    order_price = MENU[order]['cost']
    if payment < order_price:
        failed_transaction(coins=payment)
        return False
    else:
        if check_resources(order=order, resources=resources, customer_payment=payment):
            say_enjoy(order=order)
            if payment > order_price:
                remaining = payment - order_price
                print(f"💲>>> Please take Your remaining money.⬇️\n💲>>> ${format(remaining, '.2f')}")
            return True


def coffee_machine():
    new_order = True
    while new_order:
        order = process_order(order=get_order())
        if order == 'off':
            new_order = False
        elif order == 'report':
            new_order = True
        elif order == 'wrong':
            new_order = True
        else:
            customer_order = order
            customer_payment = process_coins(coins=get_coins())
            prepare_order(payment=customer_payment, order=customer_order, resources=resources)


if __name__ == '__main__':
    coffee_machine()
