# Check whether the given number is prime or not prime.

num=int(input("Enter a number="))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
            break
    else:
            print(num,"is a prime number")
