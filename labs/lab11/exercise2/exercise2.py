num_days = int(input())
danger_threshold = float(input())
#set variables 
danger_days = 0
total_temp = 0.0

for _ in range(num_days):
    temp = float(input())
    total_temp += temp # increment total temperature
    
    if temp > danger_threshold:
        danger_days += 1

# Calculate the average temperature  after all inputs are processed
if num_days > 0:
    average_temp = total_temp / num_days

print(danger_days)
print(f"{average_temp:.1f}")