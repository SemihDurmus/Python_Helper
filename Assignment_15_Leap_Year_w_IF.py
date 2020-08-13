# Assignment_15_Leap_Year_w_IF

year = int(input("Enter the year :"))

if year % 4 != 0 and year % 100 == 0:
    leap_indicator = "not leap"
elif year % 400 != 0:
    leap_indicator = "not leap"
else:
    leap_indicator = "leap"

print (f"{year} is {leap_indicator}")
