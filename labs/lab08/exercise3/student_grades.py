test1 , test2 , test3 , test4, test5 = 78 , 85 , 92 , 67 , 88
total_points = test1 + test2 + test3 + test4 + test5
average_score = total_points // 5
#use int so the output doesnt have decimal point
test1_percent = int((test1 / total_points) * 100)
test2_percent = int((test2 / total_points) * 100)
test3_percent = int((test3 / total_points) * 100 )       
test4_percent = int((test4 / total_points) * 100)
test5_percent = int((test5 / total_points) * 100)
print(f"test1: {test1}, test2: {test2}, test3: {test3}, test4: {test4}, test5: {test5}")



"""print(f"Total Points: {total_points}, Average Score: {average_score}") 
if average_score >= 80:
    print('above average')
else:
    print('below average')
print(f"PERCEENTAGE BREAKDOWN :  \ntest1%: {test1_percent}, test2%: {test2_percent}, test3%: {test3_percent}, test4%: {test4_percent}, test5%: {test5_percent}")
   """