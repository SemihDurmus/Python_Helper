# Assignment_12_Prime_Numbers
#Print the prime numbers which are between 1 to entered limit number (nr).

nr = int(input("Enter a range of numbers : "))
prime_list = []


for j in range(1, nr+1):
    counter = 0

    for i in range (1, j+1):
        if j % i == 0:
            counter += 1

    if (counter < 3) and (n != 0) and (n != 1):
        prime_list.append(j)

print(prime_list)