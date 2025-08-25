import employee_data
#total salary with deduction
total_salary = employee_data.basic_salary - (employee_data.basic_salary * 0.11) - (employee_data.basic_salary * 0.05) - (employee_data.basic_salary * 0.02) - 50 - 30
#overtime payment
overtime_payment = employee_data.overtime_hours * employee_data.overtime_rate
#final salary
final_salary = total_salary + overtime_payment
print(f"Total salary after deductions: ${total_salary:.2f}, Overtime payment: ${overtime_payment:.2f}, Final salary: ${final_salary:.2f}")