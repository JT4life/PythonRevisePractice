donate = float(input("Enter an amount to donate or type 0 to exit"))
total = 0.0
donations = []
while donate != 0:
    donations.append(donate)
    donate = float(input("Enter an amount to donate or type 0 to exit"))
for d in donations:
    total += d
print(total)