amount = int(input())
valid_count = 0
total_withdrawn = 0
while amount != -1:
    if amount % 20 == 0 and amount <= 500:
        valid_count += 1
        total_withdrawn += amount
    amount = int(input())

print(valid_count)      # Number of valid withdrawals
print(total_withdrawn)  # Total amount from valid withdrawals only
