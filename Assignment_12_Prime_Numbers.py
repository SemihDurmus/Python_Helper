# Assignment_12_Prime_Numbers

n = int(input("Enter a number to see whether it is a prime number : "))
counter = 0

for i in range (1, n+1):
    if n % i == 0:
        counter += 1

if (sayac < 3) and (n != 0) and (n != 1):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")  