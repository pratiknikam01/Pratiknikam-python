rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
