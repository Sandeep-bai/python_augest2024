# program for multiplcation table 

input_number=int(input( " Enter number to print  multiplication table :"))

for i in range(1,21):
    print('%02d*%02d = %03d'%(input_number,i,input_number*i))
    # print(f'{input_number} * {i} = {input_number * i}')