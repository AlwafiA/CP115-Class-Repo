# exercise2.py

age = int(input())
accidents = int(input())

# Base premium by age
if age < 25:
    base_premium = 2400
elif 25 <= age <= 50:
    base_premium = 1800
else:
    base_premium = 2000

# Penalty rules
if accidents == 0:
    penalty = 0
elif accidents <= 2:
    penalty = 300
else:
    penalty = 600

# Discount: 10% only if no accidents
if accidents == 0:
    discount_amount = int(base_premium * 0.10)
else:
    discount_amount = 0

final_premium = base_premium + penalty - discount_amount

# Print outputs for the test
print(base_premium)
print(final_premium)
print(discount_amount)
