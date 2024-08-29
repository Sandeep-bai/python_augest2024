# p8.py
# Program to check if user given year is a Leap year.

num_year = int(input("Enter the year to find the leap year :"))

if (num_year % 400 ==0 ) and (num_year % 100 ==0):
    print(num_year ,"is a leap year")

elif (num_year % 4 ==0 ) and (num_year % 100 !=0):
    print(num_year , "is a leap year")

else :
    print(num_year , " is not a leap year ")