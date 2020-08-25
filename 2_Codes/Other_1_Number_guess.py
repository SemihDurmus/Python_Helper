import random
nr = random.randint(0,20)

print("In this program, you will try to find a number between 0 and 100")
rep = 0
find = False 

while find == False:
    guess = int(input("Enter your guess : "))
    rep += 1
    if guess > nr:
        print("Go lower :\n")
    elif guess < nr:
        print("Go higher :\n")
    else:
        print(f"You made it in {rep} attempts.")
        find = True




