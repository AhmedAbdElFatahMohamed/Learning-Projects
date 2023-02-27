from CM import MENU, resources

On = True
money = 0

def enough(ingredients):
    """checks if there is enough ingredients for the order or not and returns the result"""
    for item in ingredients:
        if ingredients[item]>=resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        else:
            return True

def payment():
    """request the money from user in various currencies and returns the total amount"""
    print("please insert coins.")
    total=int(input("how many quarters?: "))*0.25
    total+=int(input("how many dimes?: "))*0.1
    total+=int(input("how many nickels?: "))*0.05
    total+=int(input("how many pennies?: "))*0.01
    return total

def paid_enough(money_recieved,price):
    """ return true if the payment was accepted , or false if not enough money"""
    if money_recieved>=price:
        change=round(money_recieved-price,2)
        global money
        money+=price
        print(f"here is ${change} dollars in change")
        return True
    else:
        print("Sorry that is not enough money . money refunded ")
        return False

def make_coffee(drink,ingredients):
    """deducts the ingredients from the avaliable resources"""
    for item in ingredients:
        resources[item]-=ingredients[item]
    print(f"here is you {drink}☕☕")


while On:
    choice = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice == "off":
        On = False
    else:
        drink=MENU[choice]
        if enough(drink["ingredients"]):
            cash=payment()
            if paid_enough(cash,drink['cost']):
                make_coffee(choice,drink['ingredients'])


