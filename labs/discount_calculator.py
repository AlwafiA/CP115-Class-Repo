# CP115 Assignment: discount_calculator
# Name: ALWAFI ABDULGADER ALAMIN
# Matric No: MC2515202741

age = input("Enter your age: ")
ticket_price = input("Enter the price of the movie ticket: ")
try:
    #Try converting data to numerical after input
    age = int(age)
    ticket_price = float(ticket_price)

    # Check for negative values
    if age < 0 or ticket_price < 0:
        print("Error")
    else:
        # Determine category and discount
        if age <= 12:
            age_category = "Children"
            discount = 0.5
        elif age <= 17:
            age_category = "Teenagers"
            discount = 0.25
        else:
            age_category = "Adults"
            discount = 0

        # Calculate final price
        discounted_price = ticket_price * (1 - discount)
        print(f"You are eligible for the {age_category} discount ({discount * 100:.0f}% off).")
        print(f"Discounted ticket price: ${discounted_price:.2f}")
# Output when failed to convert data to numerical
except ValueError:
    print("Error")
