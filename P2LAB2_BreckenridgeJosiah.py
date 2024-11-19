# Josiah Breckenridge
# 2024-10-07
# P2LAB2_Fuel_Calculation
# This program creates a dictionary with car models as keys and their respective MPG values as the values. 
# It allows the user to input a car model, input the number of miles they want to drive, 
# and calculates the amount of gas needed to travel that distance.

# Create the dictionary with car models and their MPG values
vehicle_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110.0,
    'Silverado': 26.0
}

# Get the keys from the dictionary
keys = vehicle_mpg.keys()
print(f"Available vehicles: {keys}")

# Prompt the user to input a vehicle
vehicle_choice = input("Enter a vehicle to see its MPG: ")

# Check if the input is a valid vehicle
if vehicle_choice in vehicle_mpg:
    mpg = vehicle_mpg[vehicle_choice]
    print(f"The {vehicle_choice} gets {mpg} mpg.")
    
    # Ask the user for the number of miles they want to drive
    miles = float(input(f"How many miles will you drive the {vehicle_choice}? "))
    
    # Calculate the gallons of gas needed
    gallons_needed = miles / mpg
    print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle_choice} {miles:.1f} miles.")
else:
    print("Sorry, that vehicle is not in our list.")
