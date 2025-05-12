# calculator
def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*":multiply,
    "/":divide,
}

def calculator():
    should_accumulate = True
    n1 = float(input("What is your first number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operator: ")
        n2 = float(input("What's the next number? "))
        result = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {result}")

        choice = input(f"Type 'y' to continue calculatinf with {result}, or type 'n' to start a new calculation: ")
        if choice == "y":
            n1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
