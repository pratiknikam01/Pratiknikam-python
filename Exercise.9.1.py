transactions = []

for i in range(5):
    amount = float(input(f"Enter transaction {i + 1}: "))
    transactions.append(amount)

largest = max(transactions)
average = sum(transactions) / len(transactions)

print("Transaction list:", transactions)
print("Largest transaction amount:", largest)
print("Average spend:", average)
