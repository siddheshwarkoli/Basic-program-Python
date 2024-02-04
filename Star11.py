row = int(input("Enter a number of rows: "))
for i in range(row):
    print("  "*(row-i-1)+"* "*(i+1))
for i in range(row-1):
    print("  "*(i+1)+"* "*(row-i-1))