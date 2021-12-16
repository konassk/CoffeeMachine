from menu import MENU, resources

opt = True
money = 0
balance = 0


def sufficient_ingredients(c_t):
    if c_t == "espresso":
        if MENU[c_t]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            exit()
        elif MENU[c_t]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            exit()
        else:
            return 0
    else:
        if MENU[c_t]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            exit()
        elif MENU[c_t]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            exit()
        elif MENU[c_t]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            exit()
        else:
            return 0


def sufficient_money(s_m):
    global money
    if s_m == 0:
        cost_of_coffee = MENU[coffee_type]["cost"]
        print("please insert coins")
        money += int(input("how many quarter : ")) * 0.25
        money += int(input("how many dimes? : ")) * 0.1
        money += int(input("how many nickel? : ")) * 0.05
        money += int(input("how many pennies : ")) * 0.01

        if money < cost_of_coffee:
            print("Sorry that's not enough money. Money refunded.")
            exit()
        elif money > cost_of_coffee:
            change = round(money - MENU[coffee_type]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
            money -= change
            return "transaction successfully"


def make_coffee(c):
    water = resources["water"] - MENU[c]["ingredients"]["water"]
    coffee = resources["coffee"] - MENU[c]["ingredients"]["coffee"]
    if c == "espresso":
        print("Report before purchasing coffee")
        for ingredient in resources:
            print(f"{ingredient} : {resources[ingredient]}")
        print(f"Money : {balance}")
        resources["water"] = water
        resources["coffee"] = coffee
        print("Report after purchasing coffee")

    else:
        print("Report before purchasing coffee")
        for ingredient in resources:
            print(f" {ingredient} : {resources[ingredient]}")
        print(f"Money : {balance}")
        milk = resources["milk"] - MENU[c]["ingredients"]["milk"]
        resources["water"] = water
        resources["coffee"] = coffee
        resources["milk"] = milk


while opt:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_type == "off":
        opt = False
    elif coffee_type == "report":
        for i in resources:
            print(f"{i} : {resources[i]} ")
        print(f"Money : {money} $")
    else:
        check_ingredients = sufficient_ingredients(coffee_type)
        print(sufficient_money(check_ingredients))
        make_coffee(coffee_type)
        print(f"Here is your {coffee_type}. Enjoy!")
        for i in resources:
            print(f"{i} : {resources[i]} ")
        print(f"Money : {round(money, 2)} ")
