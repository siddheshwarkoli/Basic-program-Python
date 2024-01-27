# sum of odd numbers in range

start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
sum = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        sum=sum + num
print("Sum of odd numbers in the range is ",sum)