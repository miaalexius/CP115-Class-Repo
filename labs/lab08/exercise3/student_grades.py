grade1 = 78
grade2 = 85
grade3 = 92
grade4 = 67
grade5 = 88
full_mark = 500  

#just sum of grades
total_point = grade1 + grade2 + grade3 + grade4 + grade5

average = total_point / 5

# Percentage contribution of each test to total points
percentage1 = (grade1 / total_point) * 100
percentage2 = (grade2 / total_point) * 100
percentage3 = (grade3 / total_point) * 100
percentage4 = (grade4 / total_point) * 100
percentage5 = (grade5 / total_point) * 100

# results
print("Test contributions (%):")
print(f"Test1: {percentage1:.2f}%, Test2: {percentage2:.2f}%, Test3: {percentage3:.2f}%, Test4: {percentage4:.2f}%, Test5: {percentage5:.2f}%")
print("Total Points:", total_point, "out of", full_mark)
print("Average Score:", average)
