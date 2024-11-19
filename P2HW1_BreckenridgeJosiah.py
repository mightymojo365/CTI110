# Josiah Breckenridge
# Date: 10/11/2024
# Assignment: P2HW1_TravelExpenses
# This program calculates and displays travel expenses in a neatly formatted manner.

# Collect inputs from the user
initial_budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
fuel = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
total_expenses = fuel + accommodation + food
remaining_balance = initial_budget - total_expenses

# Display the results
print("\n------------Travel Expenses------------")
print(f"{'Location:':<15} {destination}")
print(f"{'Initial Budget:':<15} ${initial_budget:,.2f}")
print(f"{'Fuel:':<15} ${fuel:,.2f}")
print(f"{'Accommodation:':<15} ${accommodation:,.2f}")
print(f"{'Food:':<15} ${food:,.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':<15} ${remaining_balance:,.2f}")
