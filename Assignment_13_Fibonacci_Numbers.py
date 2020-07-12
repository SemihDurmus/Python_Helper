# Assignment_13_Fibonacci_Numbers

# Create a list of fibonacci numbers from 1 to 55
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

fi_nu = []

for i in range (-2,8):
    if i < 0 : 
        fi_nu.append(1)
    else:
        fi_nu.append(fi_nu[i] + fi_nu[i+1])

print(fi_nu)
