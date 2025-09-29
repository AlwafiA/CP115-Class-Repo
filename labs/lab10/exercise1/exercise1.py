# exercise1.py

position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here
if position == 'Manager':
    hourly_rate = 35
elif position == 'Supervisor':
    hourly_rate = 25
else: # Staff
    hourly_rate = 18

if overtime_hours > 0:
    base_overtime_pay = overtime_hours * hourly_rate * 1.5
    weekend_bonus = 0
    if is_weekend == 'Yes':
        weekend_bonus = overtime_hours * 6
    overtime_pay = base_overtime_pay + weekend_bonus
else:
    overtime_pay = 0

total_pay = overtime_pay

print(hourly_rate)
print(int(overtime_pay))
print(int(total_pay))