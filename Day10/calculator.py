from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def exponent(n1, n2):
    return n1 ** n2
def modulo(n1, n2):
    return n1 % n2

op_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent,
    "%": modulo
}
def calculator():
    should_accumulate = True
    num1 = float(input("Enter the first number: "))
    while should_accumulate:
        for symbol in op_dict:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        if operation in op_dict:
            op = op_dict[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {op}")
        else:
            print("Please enter the correct operation")
        more = input(f"Type 'y' to continue the calculation with {op} or 'n' to start a new calculation: ")
        if more == "y":
            num1 = op
        elif more == "n":
            num1 = int(input("Enter the first number: "))
        else:
            should_accumulate = False
            print("Please enter either 'y' or 'n'")

calculator()