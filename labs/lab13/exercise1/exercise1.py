correct_password = "python123"
attempts_used = 0
login_successful = False
while attempts_used < 3 and not login_successful:
    entered_password = input("Enter your password: ")
    attempts_used += 1
    if entered_password == correct_password:
        login_successful = True
        print("Login successful!")
    else:
        print("Incorrect password. Try again.")

print(login_successful)
print(attempts_used)