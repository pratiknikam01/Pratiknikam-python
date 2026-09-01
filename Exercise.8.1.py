first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

first_name = first_name.strip().title()
last_name = last_name.strip().title()

full_name = first_name + " " + last_name
print("Full name:", full_name)
