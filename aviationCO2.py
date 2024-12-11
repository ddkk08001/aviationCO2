import os
import sys

os.system('clear')

def print_red_background(text):
    sys.stdout.write("\033[41m{}\033[0m\n".format(text))

while True:
    timeFlying = input("Enter the time flying in hours: ")

    try:
        timeFlying = float(timeFlying)
        if timeFlying > 0:
            break
        else: 
            os.system('clear')
            print_red_background("Error: Flying time must be valid number. Please enter a positive integer.")
    except ValueError:
        os.system('clear')
        print_red_background("Error: Flying time must be valid number. Please enter a positive integer (WITHOUT UNITS).")

def calculateB738Fuel(timeFlying):
    return (13.75 * timeFlying)

def calculateA320Fuel(timeFlying):
    return (13.5 * timeFlying)

def calculateB789Fuel(timeFlying):
    return (18.92 * timeFlying)

def calculateB77WFuel(timeFlying):
    return (20.38 * timeFlying)

def calculateB738CO2(timeFlying):
    return (3.16 * calculateA320Fuel(timeFlying))

def calculateA320CO2(timeFlying):
    return (3.16 * calculateA320Fuel(timeFlying))

def calculateB789CO2(timeFlying):
    return (3.16 * calculateB789Fuel(timeFlying))

def calculateB77WCO2(timeFlying):
    return (3.16 * calculateB789Fuel(timeFlying))

print (timeFlying)

print(calculateB789Fuel(timeFlying), "kg/passenger")
print(calculateB789CO2(timeFlying), "kg/passenger")


#1