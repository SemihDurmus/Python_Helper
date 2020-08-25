# Assignment_5_Leap_Year

year = int(input("Enter the year :"))

leap = (year % 4 == 0) and not(year % 100 == 0) or (year % 400 == 0)

#output = f"It is {leap} that {year} is a leap year"

print(leap * f"{year} is a leap year")
print((not leap) * f"{year} is a not leap year")