# WAP to Check wheather a number is armstrong or not

num = int(input("Enter a number: "))
sum = 0
order=len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** order
    temp=temp// 10
if num==sum:
    print("Given number is an armstrong number")
else:
    print("Given number is not an armstrong number")