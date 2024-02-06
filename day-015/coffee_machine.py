from coffee_resources import MENU, resources

is_working = True

money = 0

def print_resources():
    print(f'{"Water"}: {resources["water"]}ml')
    print(f'{"Milk"}: {resources["milk"]}ml')
    print(f'{"Coffee"}: {resources["coffee"]}g')
    print(f'{"Money"}: $ {money}')

def check_resources(item):
    item_resources = MENU[item]
    
    has_ingredients = True

    for ingredient in item_resources['ingredients']:
        if resources[ingredient] < item_resources['ingredients'][ingredient]:
            has_ingredients = False
    
    return has_ingredients

def process_coins(cost):
    has_money = True

    coins = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickles": 0.05,
        "pennies": 0.01
    }
    
    total = 0

    for key in coins:
        quantity = int(input(f"{key}: "))
        total += coins[key] * quantity
    
    if total < cost:
        has_money = False
        print("Sorry that's not enough money. Money refunded")
    else:
        global money
        money += cost

        if item["cost"] < total:
            difference = round(total - cost, 2)
            print(f"Here is ${difference} dollars in change.")

    return has_money
    

while is_working:

    user_option = input('What would you like? (espresso/latte/cappuccino)')

    match user_option:
        case 'off':
            print('Coffee Machine is turning off.')
            is_working = False
        
        case 'report':
            print_resources()
        
        case _:
            item = MENU[user_option]

            if not check_resources(user_option):
                print("Sorry there is not enough resources")
            
            elif process_coins(item["cost"]):
                for ingredient in item['ingredients']:
                    resources[ingredient] -= item['ingredients'][ingredient]
                print("Here is your latte. Enjoy!")
