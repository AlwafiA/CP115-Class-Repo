score1 = input("Enter score 1: ")
score2 = input("Enter score 2: ")     
score3 = input("Enter score 3: ")
total_score = float(score1) + float(score2) + float(score3)
average_score = total_score / 3

print()
print("Scores:" + str(score1) + ", " + str(score2) + ", " + str(score3))
print("Total Score: " + str(total_score))
print("Average Score: " + str(average_score))