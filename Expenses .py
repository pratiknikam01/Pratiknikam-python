print("==== Expense Tracker ====")

food = 0
travel = 0
shopping = 0

while True:
    category = input("Enter category (Food/Travel/Shopping) or 'done': ")

    if category.lower() == "done":
        break

    amount = float(input("Enter expense: "))

    if category.lower() == "food":
        food = food + amount
    elif category.lower() == "travel":
        travel = travel + amount
    elif category.lower() == "shopping":
        shopping = shopping + amount
    else:
        print("Invalid category")

total = food + travel + shopping

print("\nCategory-wise Expenses")
print("Food:", food)
print("Travel:", travel)
print("Shopping:", shopping)
print("Total Expense:", total)