# Josiah Breckenridge
# 2024-11-18
# Self-Checkout Change Calculator
# This program simulates a customer using a self-checkout machine. A random amount of money is generated as the total owed. The user inputs how much they put in the machine, and the program calculates the change required, displaying how it is given in dollars, quarters, dimes, nickels, and pennies.

import random

def disperse_change(change):
    # Calculate dollars, quarters, dimes, nickels, and pennies
    dollars = int(change // 1)
    change -= dollars
    quarters = int(change // 0.25)
    change -= quarters * 0.25
    dimes = int(change // 0.10)
    change -= dimes * 0.10
    nickels = int(change // 0.05)
    change -= nickels * 0.05
    pennies = round(change / 0.01)  # Rounding to account for floating-point precision errors

    # Display the change details
    if dollars > 0:
        print(f"{dollars} Dollar(s)")
    if quarters > 0:
        print(f"{quarters} Quarter(s)")
    if dimes > 0:
        print(f"{dimes} Dime(s)")
    if nickels > 0:
        print(f"{nickels} Nickel(s)")
    if pennies > 0:
        print(f"{pennies} Penny/Pennies")

def main():
    # Generate a random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed}")

    # Prompt user to enter the amount they will put into the self-checkout
    cash_given = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change owed
    if cash_given < total_owed:
        print("Insufficient cash provided.")
    else:
        change = round(cash_given - total_owed, 2)
        print(f"Change is: ${change}")
        # Call the disperse_change function to display the change breakdown
        disperse_change(change)

# Run the main function
if __name__ == "__main__":
    main()
