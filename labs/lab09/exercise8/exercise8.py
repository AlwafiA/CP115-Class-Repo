
income = int(input())
employment = input()
credit = input()
years = int(input())



criteria_met = 0


if income >= 3000:
    criteria_met += 1


if employment in ["permanent", "contract"]:
    criteria_met += 1


if credit in ["excellent", "good"]:
    criteria_met += 1


if years >= 2:
    criteria_met += 1



if criteria_met == 4:
    approval_status = "Approved"
elif criteria_met == 3:
    approval_status = "Conditionally Approved"
else:
    approval_status = "Rejected"

print(approval_status)