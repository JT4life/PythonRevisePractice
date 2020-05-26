item1 = 50
item2 = 10
item3 = 20
item4 = 40
items = 0
total = 0.0

enter = int(input("How many items are you buying?"))

while enter <= 5 or total <= 100:
    itemBuy = int(input("Enter '1 for item1' '2 item2' '3 item3' '4 item4' or 0 to exit"))
    if itemBuy == 1:
        itemBuy = item1
        total += itemBuy
        if total >= 100:
            break
    elif itemBuy == 2:
        itemBuy = item2
        total += itemBuy
        if total >= 100:
            break
    elif itemBuy == 3:
        itemBuy = item3
        total += itemBuy
        if total >= 100:
            break
    elif itemBuy == 4:
        itemBuy = item4
        total += itemBuy
        if total >= 100:
            break
    else:
        break
print(total)