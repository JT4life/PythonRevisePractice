total = 0.0
tax = 0.0
userInput = input("What country are you from?")
userTotal = float(input("and what is your order total?"))
if userInput == "Canada":
    n = input("Which province? Ontario, New Brunswick, Nova Scotia")
    if n == "Ontario" or "New Brunswick" or "Nova Scotia":
        tax = .13
        total = userTotal * tax
        print(userTotal + total)
    else:
        tax = .06
        total = userTotal*tax
        print(userTotal+total)
elif userInput != "Canada":
    print(userTotal)


