age_input = input()

ages = [int(age) for age in age_input.split()]
age_count = len(ages)
total_age = sum(ages)
average_age = total_age / age_count if age_count > 0 else 0

print(age_count)
print(total_age)
print(f"{average_age:.2f}")
