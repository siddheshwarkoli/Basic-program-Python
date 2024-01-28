# WAP to check the given number is perfect square number or not

num= int(input("Enter a number: "))
root=num**0.5
print(root)
sr=int(root)
print(sr)
if sr==root:
    print("Given number is perfect square number")
else:
    print("Given number is not perfect square number")