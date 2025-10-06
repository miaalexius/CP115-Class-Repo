# Stage 1: Basic grade calculation
marks = 45
total_marks = 100

percentage = (marks / total_marks) * 100
print(f"Student scored: {percentage}%")


if percentage >= 90:
    print("Grade: A - Excellent!")
elif percentage >= 80:
    print("Grade: B - Good!")
elif percentage >= 70:
    print("Grade: C - Satisfactory!")
elif percentage >= 60:
    print("Grade: D - Pass!")
else:
    print("Grade: F - Fail!")