days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["9-10", "10-11", "11-12", "12-1", "1-2"]

schedule = [["-" for _ in days] for _ in hours]


def display_schedule():
    print("\n" + "=" * 75)
    print("CLASS SCHEDULE")
    print("=" * 75)

    print(f"{'Time':<10}", end="")
    for day in days:
        print(f"{day:<13}", end="")
    print()

    for i, hour in enumerate(hours):
        print(f"{hour:<10}", end="")
        for j in range(len(days)):
            print(f"{schedule[i][j]:<13}", end="")
        print()

    print("=" * 75)


while True:
    display_schedule()

    print("\n1. Add/Overwrite Subject")
    print("2. View Subject")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nDays:")
        for i, day in enumerate(days, start=1):
            print(f"{i}. {day}")

        day_choice = int(input("Select day (1-5): "))

        print("\nTime Slots:")
        for i, hour in enumerate(hours, start=1):
            print(f"{i}. {hour}")

        hour_choice = int(input("Select hour slot (1-5): "))

        if 1 <= day_choice <= 5 and 1 <= hour_choice <= 5:
            topic = input("Enter subject/topic: ")
            schedule[hour_choice - 1][day_choice - 1] = topic
            print("Schedule updated successfully!")
        else:
            print("Invalid day or time slot.")

    elif choice == "2":
        day_choice = int(input("Enter day number (1-5): "))
        hour_choice = int(input("Enter hour slot number (1-5): "))

        if 1 <= day_choice <= 5 and 1 <= hour_choice <= 5:
            topic = schedule[hour_choice - 1][day_choice - 1]
            print(f"Subject: {topic}")
        else:
            print("Invalid day or time slot.")

    elif choice == "3":
        print("Schedule system closed.")
        break

    else:
        print("Invalid choice. Please try again.")