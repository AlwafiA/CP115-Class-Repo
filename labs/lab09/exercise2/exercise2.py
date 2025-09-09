employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# Constants
total_overtime_pay = overtime_hours * 35
epf = 0.11
socso = 0.005
total_salary = base_salary + total_overtime_pay

# Determine tax rate
if (total_salary >= 5000) and ((tax_status == "Single")):
    tax_rate = "22%"
    rate = 0.22
elif (total_salary < 5000) and ((tax_status == "Single")):
    tax_rate = "18%"
    rate = 0.18
elif (total_salary >= 6000) and (tax_status == "Married"):
    tax_rate = "20%"
    rate = 0.20
elif (total_salary < 6000) and (tax_status == "Married"):
    tax_rate = "15%"
    rate = 0.15
elif (total_salary >= 5500) and (tax_status == "Head"):
    tax_rate = "25%"
    rate = 0.25
elif (total_salary < 5500) and (tax_status == "Head"):
    tax_rate = "19%"
    rate = 0.19

# Apply tax and deductions
taxed_salary = total_salary * (1 - rate)
net_salary = taxed_salary * (1 - epf - socso)

# Output
print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")