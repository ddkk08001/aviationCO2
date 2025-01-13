import os
import sys
import matplotlib.pyplot as plt

os.system('clear')

# Error Code Background Definition
def print_red_background(text):
    sys.stdout.write("\033[41m{}\033[0m\n".format(text))

# Number Input
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
 
# Fuel Used Calculation
def calculateB738Fuel(timeFlying):
    if timeFlying >= 7:
        return 0
    else:
        return (13.75 * timeFlying)

def calculateA320Fuel(timeFlying):
    if timeFlying >= 8:
        return 0
    else:
        return (13.5 * timeFlying)

def calculateB789Fuel(timeFlying):
    if timeFlying >= 17:
        return 0
    else:
        return (18.92 * timeFlying)

def calculateB77WFuel(timeFlying):

    if timeFlying >= 14:
        return 0
    else:
        return (20.38 * timeFlying)


# CO2 Emissions Calculation
def calculateB738CO2(timeFlying):
    return (3.16 * calculateB738Fuel(timeFlying))

def calculateA320CO2(timeFlying):
    return (3.16 * calculateA320Fuel(timeFlying))

def calculateB789CO2(timeFlying):
    return (3.16 * calculateB789Fuel(timeFlying))

def calculateB77WCO2(timeFlying):
    return (3.16 * calculateB77WFuel(timeFlying))

# Table Output
data = [
    ["Aircraft", "|", "Fuel (kg/passenger)", "|", "CO2 (kg/passenger)"],
    ["B737-800", "|", round(calculateB738Fuel(timeFlying), 1), "|", round(calculateB738CO2(timeFlying), 1)],
    ["A320-200", "|", round(calculateA320Fuel(timeFlying), 1), "|", round(calculateA320CO2(timeFlying), 1)],
    ["B787-9", "|", round(calculateB789Fuel(timeFlying), 1), "|", round(calculateB789CO2(timeFlying), 1)],
    ["B777-300ER", "|", round(calculateB77WFuel(timeFlying), 1), "|", round(calculateB77WCO2(timeFlying), 1)]
]

print("Table: Fuel Burned and CO2 Emissions per Passenger for Different Aircrafts")
print("-" * 70)
for row in data:
    print("{: >15} {: >2} {: >20} {: >2} {: >20}".format(*row))
    print("-" * 70)

# Explianation of 0s in Data
if (calculateB738Fuel(timeFlying) == 0 or calculateA320Fuel(timeFlying) == 0 or calculateB789Fuel(timeFlying) == 0 or calculateB77WFuel(timeFlying) == 0):
    print_red_background("Note: A 0 in the Fuel column indicates that the aircraft is not capable for flying for given hours.")
    if (calculateB738Fuel(timeFlying) == 0 and calculateA320Fuel(timeFlying) == 0 and calculateB789Fuel(timeFlying) == 0 and calculateB77WFuel(timeFlying) == 0):
        print_red_background("Note: No aircraft is capable for flying for given hours.")
    else:
        # Least CO2 Emissions
        calc_co2_values = [row[4] for row in data[1:] if row[4] != 0]
        least_value = min(calc_co2_values)  
        if least_value == round(calculateB738CO2(timeFlying), 1):
            print("The B737-800 has the least CO2 emissions per passenger.")
        elif least_value == round(calculateA320CO2(timeFlying), 1):
            print("The A320-200 has the least CO2 emissions per passenger.")
        elif least_value == round(calculateB789CO2(timeFlying), 1):
            print("The B787-9 has the least CO2 emissions per passenger.")
        else:
            print("The B777-300ER has the least CO2 emissions per passenger.")
else:
    # Least CO2 Emissions
    calc_co2_values = [row[4] for row in data[1:] if row[4] != 0]
    least_value = min(calc_co2_values)  
    if least_value == round(calculateB738CO2(timeFlying), 1):
        print("The B737-800 has the least CO2 emissions per passenger.")
    elif least_value == round(calculateA320CO2(timeFlying), 1):
        print("The A320-200 has the least CO2 emissions per passenger.")
    elif least_value == round(calculateB789CO2(timeFlying), 1):
        print("The B787-9 has the least CO2 emissions per passenger.")
    else:
        print("The B777-300ER has the least CO2 emissions per passenger.")
        

# Graph Output
aircraft = [row[0] for row in data[1:]]
fuel = [row[2] for row in data[1:]]
co2 = [row[4] for row in data[1:]]

fig1, ax1 = plt.subplots()  

color = 'tab:red'
ax1.set_xlabel('Aircraft')
ax1.set_ylabel('Fuel (kg/passenger)')
ax1.bar(aircraft, fuel, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_title('Fuel Burned and CO2 Emissions per Passenger for Different Aircrafts')

fig2, ax2 = plt.subplots()
color = 'tab:blue'
ax2.set_xlabel('Aircraft')
ax2.set_ylabel('CO2 (kg/passenger)')
ax2.bar(aircraft, co2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_title('Fuel Burned and CO2 Emissions per Passenger for Different Aircrafts')

fig1.tight_layout()
fig2.tight_layout()
plt.show()