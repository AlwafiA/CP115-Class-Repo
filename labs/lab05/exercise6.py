minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print("Minutes : "+ str(minutes))
print(f"{minutes} minutes is {hours} hours and {remaining_minutes} minutes.")

# // : ROUND OFF
# %  : RETURN THE REMAINDER (OF DIVISION ONLY)