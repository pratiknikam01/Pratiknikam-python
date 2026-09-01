text = input("Enter the text: ")

at_count = text.count("@")
hash_count = text.count("#")
exclamation_count = text.count("!")

print("\n----- EMAIL SCAN RESULT -----")
print("@ occurrences:", at_count)
print("# occurrences:", hash_count)
print("! occurrences:", exclamation_count)
