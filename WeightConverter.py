import os

print("Welcome to Celik's weight converter!")

weight = float(input("What is your weight?: "))
unit = input("Is it (K)g or (L)bs?: ")

if unit.upper() == "L":
    message = ("Your weight is: " + str(weight / 2.205) + " Kg")
elif unit.upper() == "K":
    message = ("Your weight is: " + str(weight * 2.205) + " Lbs")

print(message)

os.system('pause')
