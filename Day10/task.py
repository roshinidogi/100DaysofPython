# def format_name():
#     f_name = input("What is your first name?\n")
#     l_name = input("What is your last name?\n")
#     if f_name == "" or l_name == "":
#         return "Invalid input!"
#     return f_name.title() + " " + l_name.title()
#
# # output = format_name()
# print(f"{format_name()}.")

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(int(input("Enter the year: "))))

# n1 = int(input("What's the first number?: "))
#     operation = input("+\n-\n*\n/\nPick an operation: ")
    # n2 = int(input("What's the second number?: "))