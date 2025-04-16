# total bill calculator
print("Welcome to Pizza deliveries")
bill = 0
size = input("What is the size of ur pizza? S, M or L: ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("U made the wrong choice")
pepperoni = input("Do u want pepperoni in ur pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
cheese = input("Do u want extra cheese? Y or N: ")
if cheese == "Y":
    bill += 1
print(f"Your total bill is ${bill} dollars")