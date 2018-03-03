days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

day = int(input("Day (0-6)? "))

if day >= 0 and day <= 6:
    print(days_of_week[day])
else:
    print("That was not a valid day of the week number!")