# Task : Find out the most frequent number and its frequency.
#Write a program that;

#Finds out the most frequent number in the given list.
#Calculates its frequency. 

num = "137430363"

num_list = list(num)

most_freq = max(num_list, key=num_list.count)

repet = num_list.count(most_freq)

print(f"The most frequent number in the list is {most_freq}, and it is repeated {repet} times.")
