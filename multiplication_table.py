# Python program to display multiplication table


num=input("Enter the number=")
print("The multiplication table of ",num)
try:
    for i in range(1,11):
        print(int(num),"*",i,"=",int(num)*i)
except Exception as e :
    print(" ",e)
print("Hello Python")
