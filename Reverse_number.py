# Reverse a number using a while loop

num=int(input("Enter a number: "))
rev=0
while(num>0):
    a=num%10
    rev=rev*10+a
    num=num//10
print("The reverse number is: ",rev)
