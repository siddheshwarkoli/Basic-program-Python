#  write a program to calculate LCM of two number

num1=int(input("Enter 1st nuber: "))
num2=int(input("Enter 2nd number: "))
for i in range(1,min(num1,num2)+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)
lcm=(num1*num2)/gcd
print(lcm)