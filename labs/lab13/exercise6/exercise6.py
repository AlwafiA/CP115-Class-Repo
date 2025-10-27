age = int(input())
tickets_sold = 0
total_revenue = 0.0
while age != -1:
    if age < 5:
        price = 0.0
    elif 5 <= age <= 17:
        price = 10.0
    else:
        price = 15.0

    tickets_sold += 1
    total_revenue += price
    age = int(input())
    

print(tickets_sold)
print(total_revenue)
