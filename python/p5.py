#  Accept average score from the student of his exam and print his result as follows :
# 0 to 49 id Fail
# 50 to 74 is second class 
# 91 to 100 is distinction 
# Also check for invalid score

avg_score=int(input('Enter your score :'))


if (avg_score >=91 and avg_score <=100):
    print(f'your score is {avg_score} distinction')

elif (avg_score >=75 and avg_score <=90):
    print(f'your score is {avg_score} first class ')

elif (avg_score >=50 and avg_score <=74):
    print(f'your score is {avg_score} second class')

elif (avg_score >=0 and avg_score <=49):
    print(f'your score is {avg_score} fail')

else :
    print('invalid')



