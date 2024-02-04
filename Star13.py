rows = int(input("Enter the number of rows: "))
for i in range(0,rows):
    for j in range(i + 1):
        if j == 0 or j == i or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
