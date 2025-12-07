print("Welcome to the Tip Calculator!\n")
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
# Use replace() function to get the digits from the string
# Convert the input string to float
# bill = float(bill_str.replace("$", ""))
# tip = int(tip_str)
split = int(input("How many people to split the bill?\n"))
t = (bill*tip)/100
# split = float(split_str)
# Use the format() function with {:.2f} to limit the decimal part to only 2 digits
# print("Each person should pay: ", "$"+"{:.2f}".format((bill + t)/split))
# You can use round(output, number) function to round the output by n digits
print("Each person should pay: $",round((bill+t)/split,2))