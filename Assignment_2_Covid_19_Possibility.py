# Assignment_2_Covid_19_Possibility

"""
Task : Estimating the risk of death from coronavirus.

Consider the following questions in terms of True/False regarding someone else.

Are you a cigarette addict older than 75 years old? Variable → age

Do you have a severe chronic disease? Variable → chronic

Is your immune system too weak? Variable → immune

Set a logical algorithm using boolean logic operators (and/or) and 
the given variables in order to give us True (there is a risk of death) 
or False (there is not a risk of death) as a result.
"""
print("Estimating the risk of death from coronavirus.")

age = False 

print("You are over 75           :", age)

chronic = False

print("You have chronic diseases :", chronic)

immune = False  

print("Your immune system is weak:", immune, "\n")

risk = age or chronic or immune

print(risk * "You have high risk of death")
print((not risk) * "You are not in danger")