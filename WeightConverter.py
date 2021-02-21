print("Welcome to Celik's weight converter!")

weight = float(input("What is your weight?: "))
unit = input("Is it (K)g or (L)bs?: ")

if unit.upper() == "L":
   print("Your weight is: " + str(weight / 2.205) + " Kg")
elif unit.upper() == "K":
    print("Your weight is: " + str(weight * 2.205) + " Lbs")

#Pause

import os
os.system('pause')