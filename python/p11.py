# p11.py Program to Find Sum of digits of a number


input_number=int(input("Enter the number to find sum of digits of number :"))
sum=0
while input_number>0:
    last_number=input_number%10 # fetch the last digit
    sum=last_number+sum 
    input_number=input_number//10 # remove the last digit
print(sum)

