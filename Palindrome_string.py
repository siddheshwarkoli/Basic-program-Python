# Write a python program to check whether the given string is palindrome or not.

string=input("Enter a word=")
rev=""
for i in string:
    rev=i+rev
#print("reverse string=",rev)
if(string==rev):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
