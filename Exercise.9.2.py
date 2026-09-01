grades = list(map(float, input("Enter grades separated by spaces: ").split()))

print("Original grades:", grades)

index = int(input("Enter the index position to update: "))
new_grade = float(input("Enter the new grade: "))

grades[index] = new_grade

print("Corrected grades:", grades)

