subject1 = int(input("Enter marks for Subject 1: "))

subject2 = int(input("Enter marks for Subject 2: "))

subject3 = int(input("Enter marks for Subject 3: "))


total = subject1 + subject2 + subject3

average = total / 3


print("\n===== STUDENT SCORECARD =====")

print("Subject 1: ", subject1)

print("Subject 2: ", subject2)

print("Subject 3: ", subject3)

print("-----------------------------")

print("Total Marks: ", total)

print("Average: ", round(average,2))

print("=============================")