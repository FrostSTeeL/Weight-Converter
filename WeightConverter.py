import os

#Greeting
print("Welcome to Celik's weight converter!")

#Variables
weight = float(input("What is your weight?: "))
unit = input("Is it (K)g or (L)bs?: ")

#Computation
if unit.upper() == "L":
    message = ("Your weight is: " + (str(weight / 2.205)[0:5]) + " Kg")
elif unit.upper() == "K":
    message = ("Your weight is: " + (str(weight * 2.205)[0:5]) + " Lbs")

print(message)

os.system('pause')
