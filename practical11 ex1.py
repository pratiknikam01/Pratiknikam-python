seats = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]

while True:
    print("\nSeating Layout:")
    for row in seats:
        print(" ".join(row))

    row = int(input("Enter row (1-3), or 0 to exit: "))

    if row == 0:
        print("Booking system closed.")
        break

    col = int(input("Enter column (1-3): "))

    if 1 <= row <= 3 and 1 <= col <= 3:
        if seats[row - 1][col - 1] == "O":
            seats[row - 1][col - 1] = "X"
            print("Seat reserved successfully!")
        else:
            print("Sorry, that seat is already reserved.")
    else:
        print("Invalid row or column.")