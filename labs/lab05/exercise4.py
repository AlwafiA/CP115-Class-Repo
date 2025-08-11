item1 = input("Enter your name: ")
item1price = input("Enter your price: ")
item2 = input("Enter your name: ")
item2price = input("Enter your price: ")
item3 = input("Enter your name: ")
item3price = input("Enter your price: ")

subtotal = float(item1price) + float(item2price) + float(item3price)
tax_amount = subtotal * 0.06
total = subtotal + tax_amount
print()
print("subtotal :" + str(subtotal))
print("tax :" + str(tax_amount))   
print("total :" + str(total))

