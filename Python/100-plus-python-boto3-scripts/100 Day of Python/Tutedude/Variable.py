score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score < 80 and score >= 60:
    grade = "C"
else:
    grade = "D"
print(f"Your grade is: {grade}")