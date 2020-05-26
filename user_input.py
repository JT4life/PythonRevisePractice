ask = input("Please enter your first name")
price = float(input("Enter your unit price"))
total = float(input("Enter your total of units"))

rounded = round(total*price, 2)
print("Hello ", ask)
print("Total price = ", rounded)