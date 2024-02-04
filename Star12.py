row =int(input("Enter a row: "))
for i in range(row):
    if i == 0 or i == (row-1):
        print('*'*row)
    else:
        print('*'+' '*(row-2)+'*')










