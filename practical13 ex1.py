inventory = {
    "Apples": 10,
    "Bananas": 5,
    "Milk": 3
}

def process_sale(item, quantity):
    if item not in inventory:
        print(f"Error: {item} is not in the inventory.")
        return

    if quantity > inventory[item]:
        print(f"Not enough stock for {item}. Available: {inventory[item]}")
        return

    inventory[item] -= quantity
    print(f"Sold {quantity} {item}. Remaining stock: {inventory[item]}")

    if inventory[item] == 0:
        print(f"WARNING: {item} is now out of stock!")


process_sale("Apples", 4)
process_sale("Bananas", 5)
process_sale("Milk", 1)

print("\nCurrent inventory:")
for item, stock in inventory.items():
    print(f"{item}: {stock}")