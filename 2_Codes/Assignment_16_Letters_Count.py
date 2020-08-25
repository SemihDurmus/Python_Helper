# Assignment_16_Letters_Count
# Count the number of each letter in a sentence.


sentence = "Her gun daha ileri, hep ileri"

letter_count = {}

for i in sentence:
    keys = letter_count.keys()
    if i in keys:
        letter_count[i] +=1
    else:
        letter_count[i] =1

print(letter_count)
