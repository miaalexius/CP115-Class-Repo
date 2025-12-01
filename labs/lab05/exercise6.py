total_minutes = int(input("Enter time in minutes: "))

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print("total minutes: " , total_minutes)
print("Converted time:", hours, "hour(s) and", remaining_minutes, "minute(s)")