# WAP to list and sum all the prime numbers in range

num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))
sum=0
print("Prime numbers between", num1, "and", num2, "are:")
for num in range(num1, num2 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           sum=sum+num
print("Sum of all Prime number is: ",sum)