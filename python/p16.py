# p16 Program to reverse a number

num_input = int(input("Enter the number to find a reverse of it :"))
reversed_num = 0

while num_input > 0 :
    last_input = reversed_num *10 +num_input % 10
    num_input = num_input // 10
print(last_input)


   





