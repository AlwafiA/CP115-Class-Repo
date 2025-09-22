day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

# Determine base price only
if day_type == "Weekend":
    if customer_type == "Adult":
        base_price = 18
    elif customer_type == "Child":
        base_price = 12
    elif customer_type == "Senior":
        base_price = 15
elif day_type == "Weekday":
    if customer_type == "Adult":
        base_price = 15
    elif customer_type == "Child":
        base_price = 10
    elif customer_type == "Senior":
        base_price = 12

# Final price starts as base
final_price = base_price

# Evening surcharge
if show_time >= 19:
    final_price += 3

# Student discount (only weekdays)
if day_type == "Weekday" and is_student == "Yes":
    final_price *= 0.9
# Output results
print(base_price)
print(final_price)