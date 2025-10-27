found_number = None
for number in range(1, 101):
    if number % 7 == 0 and number % 5 != 0:
        found_number = number
        break
print(found_number)
