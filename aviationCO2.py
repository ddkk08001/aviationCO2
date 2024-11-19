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

print (timeFlying)