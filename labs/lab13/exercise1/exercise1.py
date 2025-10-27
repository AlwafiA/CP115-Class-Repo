correct_password = "python123"
attempts_used = 0
login_successful = False

while attempts_used < 3:
    entered_password = input("Enter your password: ")
    attempts_used += 1

    if entered_password == correct_password:
        login_successful = True
        break  # Stops the loop immediately if password is correct

# Only print final results (important for test to pass)
print(login_successful)
print(attempts_used)