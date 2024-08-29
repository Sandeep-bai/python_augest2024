# p15
# Program to find Sum of even(odd) digits in a number

num_input = int(input("Enter the number to find even digit :"))
count = 0 
original_num = num_input

while num_input > 0 :
    last_digit = num_input % 10 
    num_input = num_input // 10
    if last_digit % 2 == 0 :
        count = count + last_digit
    else :
        continue

print("The sum of thr even number " ,original_num , "is" , count )
    





