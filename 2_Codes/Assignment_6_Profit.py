# Assignment_6_Profit
"""
Task - 1 : You work for a manufacturer as a programmer and have been asked 
to calculate the total profit made on the sales of a product. 
You are given a dictionary (sales) containing the cost price per unit (in dollars), 
sell price per unit (in dollars), and the beginning inventory. Write a program 
to return the total profit made, rounded to the nearest dollar. 
Assume all of the inventory has been sold. 
The name and the keys of the dictionary are constant, so use them as they are.
"""

sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  

profit = (sales.get('sell_value') - sales.get('cost_value')) * sales.get('inventory')
print("Profit is $",round(profit))


# the profit will be : 13130

#profit = ((sales['sell_value'] - sales['cost_value']) * sales['inventory'])

"""
Task-2: Your boss wants you to prepare the payrolls of the workers in your department. 
You have to convert the amount of dollars into payroll format. 
In order to help move things along, you have volunteered to write a code 
that will take a float and return the amount formatting in dollars and cents.
"""

payroll = float(input("Enter the payroll "))

print('Payroll is $%.2f' %(payroll)) #.2f means let only 2 decimal digits