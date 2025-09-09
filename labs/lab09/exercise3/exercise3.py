day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

#CONSTANTS
base_price = 0
student_discount = 0.1
final_price = (base_price) * (1 - student_discount)

# DETERMINE TICKET PRICE    
if day_type == "Weekends":
    student_discount = 0
    if customer_type == "Adult":
        base_price = 18
    elif customer_type == "Child":
        base_price = 12
    elif customer_type == "Senior":
        base_price = 15
    if show_time > 1800:
        new_base = base_price + 3
elif day_type == "Weekdays":
    if customer_type == "Adult":
        base_price = 15
    elif customer_type == "Child":
        base_price = 10
    elif customer_type == "Senior":
        base_price = 12
    if show_time > 1800:
        new_base = base_price + 3
if is_student == "Yes":
    student_discount = 0.1
final_price = (base_price) * (1 - student_discount)

print(base_price)
print(final_price)