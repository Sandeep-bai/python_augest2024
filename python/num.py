def facto_iterative(num):
    fact =1 
    if num == 0 or num ==1 :
        return fact
    for i in range(2 , num + 1):
        fact = fact*i
        return fact

def facto_recursive(num):
    if num == 0 or num ==1 :
        return 1
    return num * facto_iterative(num-1)

input_num = int(input("Enter the number to find factorial :"))

choice = int(input("1 :iterative 2 : recursive . your choice please :"))


fact = 0
if choice ==1 :
    fact = facto_iterative(input_num)

else :
    fact = facto_recursive(input_num)


print(f'Factorial of {input_num} = {fact}')


# python -m pdb num.py