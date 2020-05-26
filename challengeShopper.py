ask = float(input("Enter your total purchased"))
if ask < 50:
    ask += 10
else:
    print("Shipping is free")

print("Your total is $", ask)