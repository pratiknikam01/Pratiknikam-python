print(" ==== Expenses Tracker ==== ")

expense = 0.0

while True :
    value = float(input("Enter your Expense :"))

    if value == -1 :
        break 

    expense = expense + value 

    print("Total Expense : ",expense)



    