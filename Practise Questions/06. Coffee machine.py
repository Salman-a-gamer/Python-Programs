MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

### This program is still un polished...
##
#

def check_resources(required_res, r):
    for k, v in required_res.items():
        if v > r[k]:
            return v
    for k,v in required_res.items():
        r[k] -=v
    return 1
    
    # you can use this when all the coffees have the same order of ingredients
    # for (k1,v1) , (k2,v2) in zip(required_res.items(), r.items()):
    #     if v1 > v2:
    #         return k1
    # for (k1, v1), (k2, v2) in zip(required_res.items(), r.items()):
    #     r[k2] -= v1
    #
    # print(r)
    # return 1

def report(money_earned):
    for k,v in resources.items():
        print(k+': ' + str(v))
    print('money :'+ str(money_earned) )


def calculate_change(req_money, q,d,n,p):
    money_received = q*0.25 + d*0.10 + n*0.05 + p*0.01
  #  print('total money received: ' + str(money_received))
    if req_money > money_received:
        print('Sorry. That\'s not enough money. Money refunded.')
        return -1
    else:
        return money_received - req_money

def ask_money(req_money):
    print('Please insert coins.')
    while True:
        quarters = input('How many Quarters? ')
        dimes = input('How many dimes? ')
        nickels = input('How many nickels? ')
        pennies = input('How many pennies? ')
        if not all(n.isdigit() for n in [quarters,dimes, nickels, pennies]):
            print('Please enter proper values.')
            continue
        else:
            change = calculate_change(req_money, int(quarters), int(dimes), int(nickels), int(pennies))
            if change == -1:
                return -1
            else:
                print(f"Here is ${round(change,2)} in change.")
                return change


def make_coffee(coffee, money_earned):
    required_res = MENU[coffee]['ingredients']
    missing = check_resources(required_res, resources)
    if missing != 1 :
        print(f"Sorry there's not enough {missing}")
        return -1

    change = ask_money(MENU[coffee]['cost'])
    if change == -1:
        return -1
    else:
        money_earned = MENU[coffee]['cost']
        print('Enjoy your ' + coffee)
        return money_earned


def main():
    money_earned = 0
    while True:
        request = input("What would you like? (espresso/latte/cappuccino): ")
        request = request.lower().strip()
        if request in ('espresso', 'latte', 'cappuccino'):
            m = make_coffee(request, money_earned)
            if m == -1:
                continue
            else:
                money_earned += m
        elif request == 'off':
            break
        elif request == 'report':
            report(money_earned)
main()
