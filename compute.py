import math
x=int(input("Enter value of X: "))
n=int(input("Enter value of N: "))
fact=math.factorial(n)
power=math.pow(x,n)
result=power/fact
print("result of given equestion is: ",result)