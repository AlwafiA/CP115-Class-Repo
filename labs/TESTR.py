total = 0
for day in range(1, 6):
    amount = float(input("Enter amount of plastic collected on day " +
str(day) + ": "))
    total += amount
print("Total amount of plastic collected in 5 days:",total)