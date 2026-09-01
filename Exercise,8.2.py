feedback = input("Enter your feedback: ")

target_words = ["bad", "hate"]

for word in target_words:
    feedback = feedback.replace(word, "***")

print("Filtered feedback:", feedback)
