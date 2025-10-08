# Initialize variables
age_count = 0
total_age = 0
age_input = ""

# Loop to collect ages until "done" is entered
while age_input != "done":
    # Get input from the user (expected to be an age or "done")
    age_input = input()

    # Check if the user entered an age (and not "done")
    if age_input != "done":
        try:
            # Convert the input to an integer
            age = int(age_input)
            
            # Update the count and total sum
            age_count += 1
            total_age += age
        except ValueError:
            # Handle cases where the input is not a number or "done"
            # Depending on the exact requirements, you might want to skip or error here.
            # Assuming for this problem, we only care about valid ages or "done".
            pass

# Calculate the average age
if age_count > 0:
    average_age = total_age / age_count
else:
    # Handle the case where "done" is entered immediately (to avoid division by zero)
    average_age = 0.0

# Print the required results in the exact format
print(age_count)
print(total_age)
# The test expects a float with two decimal places, even if the result is a whole number (e.g., 25.00)
print(f"{average_age:.2f}")