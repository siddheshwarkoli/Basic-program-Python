row = int(input("Enter a number of rows: "))
for i in range(row):
    print("* "*(i+1))
for i in range(row-1):
    print("* "*(row-i-1))