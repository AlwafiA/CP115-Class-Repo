item_count = 0
total_cost = 0.0

# Use a loop that continues until the sentinel value is entered
while True:
    try:
        # Get input from the user
        price_input = input()
        
        # Convert the input to a float (price)
        # This will raise a ValueError if the input is not a valid number
        price = float(price_input)
        
        # Check for the negative sentinel value
        if price < 0:
            break  # Exit the loop if a negative number is entered
        
        # If the price is 0 or positive, count and add it to the total
        item_count += 1
        total_cost += price
        
    except ValueError:
        # If the input couldn't be converted to a float (e.g., an empty line or text)
        # We simply skip this input and ask for the next one.
        pass

# Print the required results
# The output must be:
# 1. The total count of items (integer)
# 2. The total cost (float, formatted to two decimal places)
print(item_count)
print(f"{total_cost:.2f}")