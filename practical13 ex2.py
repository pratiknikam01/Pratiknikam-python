students = {
    101: "student101@example.com",
    102: "student102@example.com",
    103: "student103@example.com",
    104: "student104@example.com",
    105: "student105@example.com"
}

print("===== Student Contact Database =====")

while True:
    roll_id = input("\nEnter Roll ID (or type 'exit' to quit): ")

    if roll_id.lower() == "exit":
        print("Exiting database...")
        break

    try:
        roll_id = int(roll_id)

        if roll_id in students:
            print("Email Address:", students[roll_id])
        else:
            print("Student with this Roll ID was not found.")

    except ValueError:
        print("Please enter a valid Roll ID.")