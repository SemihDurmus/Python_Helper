# Assignment_8_Most_Frequent_Element

"""
Task : Find out the most frequent number and its frequency.

Write a program that;

Finds out the most frequent number in the given list. Calculates its frequency. Prints out the result such as :

Example

Given list: numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

Desired Output: the most frequent number is 3 and it was 4 times repeated

Note : You can/should use a useful built-in function and a method of the list operation.
"""

num = "137430363"

num_list = list(num)

most_freq = max(num_list, key=num_list.count)

repet = num_list.count(most_freq)

print(f"The most frequent number in the list is {most_freq}, and it is repeated {repet} times.")