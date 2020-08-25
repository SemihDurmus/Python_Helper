# Assignment_7_Comfortable_Words

"""
Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

A comfortable word is a word which you can type always alternating the hand you type with 
(assuming you type using a Q-keyboard and use of the ten-fingers standard).
The word will always be a string consisting of only letters from a to z.
Write a program to returns True if it's a comfortable word or False otherwise.
"""
left_letters = set("qazwsxedcrfvtgb")
right_letters = set("yhnujmikolp")

given_str = input("Enter a word: ")
given_str_set = set(given_str)

left_check = bool(given_str_set - left_letters)
right_check = bool(given_str_set - right_letters)

check = left_check and right_check

print(check * f"\"{given_str}\" is a comfortable word")
print((not check) * f"\"{given_str}\" is not a comfortable word")