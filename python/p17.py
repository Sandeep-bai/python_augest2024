# p17
# Program to Find Odd(Even) placed digits in a number


num_input = int(input("Enter the value of num_input :"))

original_num = num_input

while num_input!=0 :
    last_digt = num_input % 10 
    num_input = num_input // 10

    if last_digt % 2 != 0 :
        print(last_digt)

    else:
        continue
     
    
    






   