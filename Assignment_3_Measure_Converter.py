# Assignment_3_Measure_Converter

"""
Task-1:

Write a short Python program that asks the user to enter Celsius temperature 
(it can be a decimal number), 
converts the entered temperature into Fahrenheit degree and prints the result.
"""

celcius = int(input("Enter the temperature value in Celcius:"))

fahrenheit = celcius * 9 / 5 + 32

print("The temperature is", round(fahrenheit,2), "F")

"""
Task-2:
Write a short Python program that asks the user to enter a distance 
(it can be a decimal number) in kilometers, 
converts the entered distance into miles and prints the result.

"""

print("Enter the distance in kilometers:")
kilometers = input()
miles = int(kilometers) * 0.62137
print("The distance is", round(miles, 2), "miles")