

score = float(input("Enter graduation score (%): "))
backlogs = int(input("Enter number of active academic backlogs: "))

if score >= 70 and backlogs == 0:
    print("\n===== PLACEMENT ELIGIBILITY =====")
    print("Candidate is ELIGIBLE for placement.")
else:
    print("\n===== PLACEMENT ELIGIBILITY =====")
    print("Candidate is NOT ELIGIBLE for placement.")