
# p12
# Program to Find count of digits of a number


num_input = int(input("Enter the Sum of digit of a number :"))
original_input = num_input

count = 0




while num_input != 0:
        num_input = num_input // 10
        count  = count + 1


print("The count of a digit of a number" , original_input , "is" , count)