# write a program to calculate GCD of two number

#-------------------------With Module-------------------------

import math
num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
result=math.gcd(num1,num2)
print(result)


#-----------------------without module------------------------

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
for i in range(1,min(num1,num2)+1):
    if num1%1==0 and num2%1==0:
        gcd=i
print("GCD of given numbers is: ",gcd)