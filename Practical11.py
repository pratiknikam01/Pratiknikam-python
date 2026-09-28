# Bus Seat Reservation Layout System Using Nested Lists
# Nested list representing bus seats
# 0 = Available, 1 = Reserved

bus = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]

# Display seat layout
print("============ BUS SEAT LAYOUT ============")

for row in bus:
    for seat in row:
        if seat == 0:
            print("Available", end=" | ")
        else:
            print("Reserved", end=" | ")
    print()

# Reserve a seat using indexing
row = int(input("Enter row number (1-4): "))
seat = int(input("Enter seat number (1-4): "))

# Convert user input to list index
row_index = row - 1
seat_index = seat - 1

# Check seat availability
if bus[row_index][seat_index] == 0:
    bus[row_index][seat_index] = 1
    print("Seat reserved successfully!")
else:
    print("Sorry! Seat is already reserved.")

# Display updated layout
print("\n**************** UPDATED BUS SEAT LAYOUT *****************")

for i in range(len(bus)):
    for j in range(len(bus[i])):
        if bus[i][j] == 0:
            print("Available", end=" | ")
        else:
            print("Reserved", end=" | ")
    print()