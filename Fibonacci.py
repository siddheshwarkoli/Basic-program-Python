# Print fibonacci sequence up to n term.

i=int(input("Enter a number"))
n1=0
n2=1
count=0
if i<=0:
    print("Enter Positive Integer")
elif i==1:
    print("Fibonacci sequence upto",i,"=")
    print(n1)
else:
    print("Fibonacci Sequence=")
    while count<i:
        print(n1)
        c=n1+n2
        n1=n2
        n2=c
        count=count+1
