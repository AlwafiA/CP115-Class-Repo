num_rounds = int(input())

#Set variables
final_score = 0.0
rounds_processed = 0

for _ in range(num_rounds):
    # Check if input() is still available and valid
    user_input = input()
    if user_input.strip() and user_input.replace('.', '', 1).isdigit():
        score = float(user_input)
        if score > 100:
            final_score += score * 1.2 #add
        else:
            final_score += score
        rounds_processed += 1
    else:
        # Exit the loop if input is invalid or empty
        break

print(f"{final_score:.1f}")
print(rounds_processed)