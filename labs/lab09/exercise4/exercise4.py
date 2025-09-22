current_reading = int(input())
previous_reading = int(input())

consumption = current_reading - previous_reading

# Calculate water cost based on consumption
if consumption <= 20:
    water_cost = 0.57 * consumption
elif consumption <= 35:
    water_cost = (0.57 * 20) + (1.03 * (consumption - 20))
else:
    water_cost = (0.57 * 20) + (1.03 * 15) + (1.40 * (consumption - 35))

#plus service charges
total_bill = water_cost + 8 + 2

print(consumption)
print((water_cost))
print((total_bill))

# adding a "current : " in input causes error
