main_dish = 25
appetizer = 12
drinks = 8
total = (3 * main_dish) + (2 * appetizer) + (4 * drinks)
plus_tax = int((total * 0.10) + total)
split_bill = plus_tax // 6
print(f"Total bill each must pay: ${split_bill}")
