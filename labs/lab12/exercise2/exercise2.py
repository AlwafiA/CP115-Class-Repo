import sys

score_count = 0
total_score = 0.0

# Read all lines from input at once to avoid an EOFError
all_lines = sys.stdin.readlines()

for line in all_lines:
    score_input = line.strip()
    
    # Manually validate if the string is a valid number to avoid a ValueError
    if score_input and score_input.replace('.', '', 1).lstrip('-').isdigit():
        score = float(score_input)
        
        # Stop the loop if the score is a negative number
        if score < 0:
            break
            
        # Process the score only if it is within the valid range (0-100)
        if 0 <= score <= 100:
            score_count += 1
            total_score += score
    else:
        # Ignore the line if it's not a valid number (e.g., text or empty)
        continue

# Calculate the average, preventing division by zero
average_score = total_score / score_count if score_count > 0 else 0.0

# Print the final results in the required format
print(score_count)
print(total_score)
print(f"{average_score:.2f}")