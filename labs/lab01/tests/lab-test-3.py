# ALWAFI ABDULGADER ALAMIN 
"""
PROBLEM DESCRIPTION:

PASU Telecommunication Company is one of the mobile line service providers
in Malaysia.
This company has made a promotion by giving a discount based on the amount
of bill payment every month as in the table below.
You are required to create a Python program that asks the user to enter the
monthly usage and then calculates and displays the amount of the bill to be paid
after receiving the discount.
"""

# Set Variables
monthly_usage = float(input("Monthly Usage : "))
discount_rate = 0

if monthly_usage < 50:
    discount_rate = 0
elif monthly_usage <= 100:
    discount_rate = 0.05
else:
    discount_rate = 0.2

# Calculate discount amount and final bill
discount_amount = monthly_usage * discount_rate
final_bill = monthly_usage - discount_amount

print(final_bill)


