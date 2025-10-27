grade = float(input())
valid_count = 0
total_sum = 0.0
while grade >= 0:
    valid_count += 1
    total_sum += grade
    grade = float(input())
average = total_sum / valid_count if valid_count > 0 else 0.0

print(valid_count)
print(f"{average:.2f}")
