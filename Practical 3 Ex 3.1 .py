

age = int(input("Enter your age: "))
income = float(input("Enter your annual family income: "))

if age < 25 and income < 300000:
    print("\n Congratulations!")
    print("You are eligible for the specialised education scholarship.")
else:
    print("\n Sorry!")
    print("You are not eligible for the specialised education scholarship.")