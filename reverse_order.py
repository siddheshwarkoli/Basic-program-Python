# Write a program which accept the users first and last name and print in reverse order

a=input("Enter your First Name: ")
b=input("Enter your Last Name: ")
full_name=a+" "+b
rev=full_name[::-1]
print("Your name in reverse order is: ",rev)
