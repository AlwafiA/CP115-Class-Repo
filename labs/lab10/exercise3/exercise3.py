# exercise3.py

monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# Default values
interest_rate = 0.0
max_loan_amount = monthly_income * 5
approval_status = "Rejected"

# Credit-based rules
if credit_score >= 700:
    interest_rate = 3.5
elif 600 <= credit_score < 700:
    interest_rate = 5.5
else:
    interest_rate = 0.0  # poor credit

# Approval logic
if credit_score >= 600 and monthly_income >= 4000 and loan_amount <= max_loan_amount:
    approval_status = "Approved"
else:
    approval_status = "Rejected"

print(interest_rate)
print(max_loan_amount)
print(approval_status)
