# Tip calculator
print("Welcome to the  tip calculator!")
value = float(input("What is the total bill? $"))
tip = int(input("How much tip would u like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_w_tip = (tip / 100) * value + value
total = round(bill_w_tip / people, 2)
print("Your total is $" + str(total))
