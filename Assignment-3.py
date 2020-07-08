# Task:

# Find out if a given number is an "Armstrong Number".

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
