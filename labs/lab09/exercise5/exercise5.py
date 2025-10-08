main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# Item prices
main_course_prices = {
    "Steak": 15.00,
    "Chicken": 10.00,
    "Vegetarian": 8.00,
    "Beef": 12.00,
    "Fish": 11.00
}
drink_prices = {
    "Soft Drink": 2.00,
    "Juice": 3.00,
    "Water": 1.00,
    "Coffee": 3.00
}
dessert_prices = {
    "Ice Cream": 4.00,
    "Cake": 5.00,
    "Fruit": 3.00
}

# Calculate the subtotal
main_course_price = main_course_prices.get(main_course, 0)
drink_price = drink_prices.get(drink, 0)
dessert_price = dessert_prices.get(dessert, 0)
total_bill = main_course_price + drink_price + dessert_price

# Add the 10% service charge
bill_with_service = total_bill * 1.10

# Apply age-based discounts
if customer_age >= 65:
    # 15% discount for seniors
    final_bill = bill_with_service * 0.85
elif customer_age < 18:
    # 10% discount for students
    final_bill = bill_with_service * 0.90
else:
    final_bill = bill_with_service

print(f"{final_bill:.2f}")