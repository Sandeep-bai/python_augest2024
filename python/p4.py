# program to Accept to  3 distinct number and find smallest amoung

input_num1=int(input('enter the first_number :'))
input_num2=int(input('enter the second_number :'))
input_num3=int(input('enter the third_number :'))

if(input_num1<input_num2 and input_num1<input_num3):
    print(f'the number {input_num1} is smallest')

elif(input_num2<input_num1 and input_num2<input_num3):
    print(f'the number {input_num2} is smallest')
    
else:
    print(f'the number {input_num3} is smallest')