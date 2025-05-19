# Coffee machine

Menu = {
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

ingredients = {"water": 300, "milk": 200, "coffee": 50}
should_continue = True

def check_resources(choice):
    required = Menu[choice]["ingredients"]
    for item, amount in required.items():
        if ingredients[item] < amount:
            print(f" Sorry, there's not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters (0.25)?: ")) * 0.25
    dimes = int(input("How many dimes (0.10)?: ")) * 0.10
    nickels = int(input("How many nickels (0.05)?: ")) * 0.05
    pennies = int(input("How many pennies (0.01)?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return round(total, 2)

def check_payment(total_inserted, choice):
    cost = Menu[choice]["cost"]
    if total_inserted < cost:
        print(" Not enough money. Money refunded.")
        return False
    else:
        change = round(total_inserted - cost, 2)
        if change > 0:
            print(f" Here's ${change} in change.")
        return True

def make_coffee(choice):
    required = Menu[choice]["ingredients"]
    for item, amount in required.items():
        ingredients[item] -= amount
    print(f" Here's your {choice}! Enjoy!")

def question():
    global should_continue
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice in ["espresso", "latte", "cappuccino"]:
        if check_resources(choice):
            total_inserted = process_coins()
            if check_payment(total_inserted, choice):
                make_coffee(choice)
    elif choice == "report":
        print("\n--- Current Resources ---")
        print(f"Water: {ingredients['water']}ml")
        print(f"Milk: {ingredients['milk']}ml")
        print(f"Coffee: {ingredients['coffee']}g")
    elif choice == "off":
        should_continue = False
        print(" Machine turned off.")
        return
    else:
        print(" Invalid choice. Please try again.")
    
    question()

print("--- Coffee Machine ---")
while should_continue:
    question()