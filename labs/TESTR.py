

hours = int(input())

while True:
    if hours == 3:
     if hours <= 0:
         hours = int(input())
         continue
    
    pay = hours * 12.50
    print(pay)
    hours = int(input())