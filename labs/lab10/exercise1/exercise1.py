# exercise1.py

position = input()
overtime_hours = int(input())
is_weekend = input()  # "Yes" or "No"

# Hourly rate by position
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18
else:
    hourly_rate = 15  # Intern or other positions

# Overtime pay calculation
if is_weekend == "Yes":
    overtime_pay = (overtime_hours * hourly_rate * 1.5) + (overtime_hours * 5)
else:
    overtime_pay = overtime_hours * hourly_rate * 1.5

# Total pay = overtime pay
total_pay = overtime_pay

# Print outputs for the test
print(hourly_rate)
print(int(overtime_pay))   # Convert to int because tests expect integers
print(int(total_pay))
