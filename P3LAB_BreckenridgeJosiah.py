# P3LAB_LastnameFirstname.py
# Program to calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies

def calculate_change(amount):
    # Convert amount to cents to avoid floating point precision issues
    cents = int(round(amount * 100))
    
    dollars = cents // 100
    cents = cents % 100
    
    quarters = cents // 25
    cents = cents % 25
    
    dimes = cents // 10
    cents = cents % 10
    
    nickels = cents // 5
    pennies = cents % 5
    
    # Display the results
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        print("No change")

# Get user input
try:
    amount = float(input("Enter the amount of money as a float: $"))
    calculate_change(amount)
except ValueError:
    print("Please enter a valid float value.")
