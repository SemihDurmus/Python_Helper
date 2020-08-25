#Assignment_1_Weekly_Profit

# If you had deposited a coin on the cryptocurrency exchange 
#that brought 7% fixed profit daily for a week, 
#how much would your $ 1000 reach at the end of the 7th day?

deposit = 1000

profit = 0.07


print("You have $", deposit, "as initial deposit\nThe profit ratio is: ", int(profit*100), "%")



deposit += profit * deposit #new deposit = deposit + profit ratio times deposit

deposit += profit * deposit #2nd day

deposit += profit * deposit #3rd day

deposit += profit * deposit #4th day

deposit += profit * deposit #5th day

deposit += profit * deposit #6th day

deposit += profit * deposit #7th day



print("At the end of the 7th day your deposit will be : $", int(deposit) ) 

"""
deposit = 1000

print("You have $", deposit, "as initial deposit\nThe profit ratio is: ", int(deposit * 0.07), "% \n")

# deposit = deposit * 0.07 * deposit
# deposit = deposit (1 + 0.07)
# deposit = deposit * 1.07 .........

deposit = deposit * (1.07 **7)

print("At the end of the 7th day your deposit will be : $", int(deposit) ) 

"""