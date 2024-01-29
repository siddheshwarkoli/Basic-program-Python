# write a program to reverse a number

num = int(input("Enter an integer: "))
string = str(num)
reverse_string = string[::-1]
reverse_number = int(reverse_string)
print("The reversed number is: ",reverse_number)