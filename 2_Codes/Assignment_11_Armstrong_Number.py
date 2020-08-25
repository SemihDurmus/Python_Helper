# Assignment_11_Armstrong_Number

"""
Task:

Find out if a given number is an "Armstrong Number".

An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. 
Examples : 371 = 3^3 + 7^3 + 1^3; 9474 = 9^4 + 4^4 + 7^4 + 4^4; 93084 = 9^5 + 3^5 + 0^5 + 8^5 + 4^5

Write a Python program that; 
-takes a positive integer number from the user, 
-checks the entered number if it is Armstrong, 
-consider the negative, float and any entries 
other than numeric values then display a warning message to the user.
"""

nr = input("Enter a number :\n ")

numbers_set = set("0123456789")

nr_valid = False

while not nr_valid: 
    if nr.isdigit():
        nr_valid = True
    elif nr[0] == "-":
        nr = input("Please enter a positive number :\n ")         
    elif ("," in nr) or ("." in nr):
        nr = input("Please enter an integer :\n ")
    elif (numbers_set & set(nr)) == set():
        nr = input("Do not use any entries other than numeric values :\n ")
    else:
        nr = input("Enter something valid :\n ")
        
        
i = 0
sum = 0

for i in (range(len(nr))):
    sum += (int(nr[i]) ** (len(nr)))

if sum == int(nr):
    print(f"{nr} is an Armstrong Number")
else:
    print(f"{nr} is not an Armstrong Number")    
