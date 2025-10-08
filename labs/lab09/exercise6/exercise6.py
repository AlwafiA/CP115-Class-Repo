position = input()
overtime_hours = int(input())
is_weekend = input()


pay_rates = {
    "Manager": 30.0,
    "Supervisor": 20.0,
    "Staff": 15.0,
    "Intern": 8.0
}
base_rate = pay_rates.get(position, 0)

overtime_pay = 0


if overtime_hours > 8:
    
    first_8_hours_pay = 8 * base_rate * 1.5
   
    remaining_hours_pay = (overtime_hours - 8) * base_rate * 2.0
    overtime_pay = first_8_hours_pay + remaining_hours_pay
else:
    # If 8 hours or less, all hours are paid at 1.5x the base rate
    overtime_pay = overtime_hours * base_rate * 1.5

# 2. Add a weekend bonus of RM5 per hour if applicable
if is_weekend == "Yes":
    weekend_bonus = overtime_hours * 5.0
    overtime_pay += weekend_bonus

# 3. Print the final calculated overtime pay
print(overtime_pay)