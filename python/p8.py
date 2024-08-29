# perfect suare 
import math
input_number=int(input("Enter the number to find perfect  square :"))

num=int(math.sqrt(input_number))

if num*num==input_number:
    print(f'{input_number} is a perfect square ')

else :
     print(f'{input_number} is not  a perfect square ')





