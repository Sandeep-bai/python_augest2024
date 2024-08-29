
# p13
# Program to find biggest (smallest) digit in a number

num_input = int(input("Enter the digit to find biggest of it :"))
original_num =  num_input
biggest_num = 0
while num_input > 0 :
    last_digit = num_input % 10 
    num_input = num_input // 10
    if last_digit > biggest_num :
        biggest_num = last_digit
    else :
        continue
print(biggest_num , "is a biggest digit in a " , original_num)

    


   
    