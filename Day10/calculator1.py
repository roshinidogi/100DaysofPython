# from art import logo
# print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
op_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
print(op_dict["*"](4, 8))
# def n_operation(n1, operation, n2):
#     # n1 = int(input("Enter the first number: "))
#     # operation = input("+\n-\n*\n/\nPick an operation: ")
#     # n2 = int(input("Enter the next number: "))
#     if operation == "+":
#         op = n1 + n2
#         return op
#     elif operation == "-":
#         op = n1 - n2
#         return print(f"{n1} {operation} {n2} = {op}")
#     elif operation == "*":
#         op = n1 * n2
#         return print(f"{n1} {operation} {n2} = {op}")
#     elif operation == "/":
#         op = n1 / n2
#         return print(f"{n1} {operation} {n2} = {op}")
#     else:
#         return print("Invalid operation")
# # def y_operation2(n1, n2, operation):
# #     # operation = input("+\n-\n*\n/\nPick an operation: ")
# #     # n2 = int(input("Enter the next number: "))
# #     if operation == "+":
# #         op = n1 + n2
# #         print(f"{n1} {operation} {n2} = {op}")
# #     elif operation == "-":
# #         op = n1 - n2
# #         print(f"{n1} {operation} {n2} = {op}")
# #     elif operation == "*":
# #         op = n1 * n2
# #         print(f"{n1} {operation} {n2} = {op}")
# #     elif operation == "/":
# #         op = n1 / n2
# #         print(f"{n1} {operation} {n2} = {op}")
# #     else:
# #         print("Invalid operation")
# while True:
#     n_operation(n1 = int(input("What's the first number?: ")), operation = input("+\n-\n*\n/\nPick an operation: "), n2 = int(input("What's the second number?: ")))
#     print(f"{n1} {operation} {n2} = {op}")
#     more = input(f"Type 'y' to continue the calculation with {op} or 'n' to start a new calculation: ")
#     if more == "y":
#         n_operation(op, operation = input("+\n-\n*\n/\nPick an operation: "), n2 = int(input("What's the second number?: ")))
#
#     elif more == "n":
#         n_operation(n1 = int(input("What's the first number?: ")), operation = input("+\n-\n*\n/\nPick an operation: "), n2 = int(input("What's the second number?: ")))
#     else:
#         break