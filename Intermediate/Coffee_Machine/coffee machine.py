from main import MENU, resources

print("Welcome to the Coffee Machine!")

def report():

    return ("Water: " + str(resources["water"]) + "ml\n"
          "Milk: " + str(resources["milk"])+ "ml\n"
          "Coffee: " + str(resources["coffee"])+ "g\n"
          "Money: $" + str(money))

def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def money_counter():
    print("Please insert coins.")
    total_money = int(input("How many quarters?: ")) * 0.25
    total_money += int(input("How many dimes?: ")) * 0.1
    total_money += int(input("How many nickles?: ")) * 0.05
    total_money += int(input("How many pennies?: ")) * 0.01
    return total_money

def make_coffee(drink_name, ingredients):
    print(f"Here is your {drink_name}. Enjoy it!")
    for item in ingredients:
        resources[item] -= ingredients[item]



money = 0.0

while True:

    request = input("What would you like? (espresso/latte/cappuccino): ")
    
    if request == "off":
        break
    elif request == "report":
        print(report())
        
    else:
        drink = MENU[request]
        if check_resources(drink["ingredients"]):
            money_have = money_counter()
            if money_have >= MENU[request]["cost"]:
                drink_cost = MENU[request]["cost"]
                print(f"Here is {round(money_have - drink_cost, 2)} in change.")
                make_coffee(request, drink["ingredients"])
                
                money += drink_cost

            else:
                print("Sorry that's not enough money. Money refunded.")

    
