days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

day = int(input("Day (0-6)? "))

if day == 0 or day == 6:
    print("Sleep in")
elif day > 6 or day < 0:
    print("That is not a valid day of the week number!")
else:
    print("Go to work")