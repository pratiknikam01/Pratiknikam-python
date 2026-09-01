paragraph = input("Enter a paragraph: ")

paragraph = paragraph.lower()

words = paragraph.split()

count = words.count("python")

print("\n----- WORD COUNT -----")
print("The word 'python' appears", count, "times.")
