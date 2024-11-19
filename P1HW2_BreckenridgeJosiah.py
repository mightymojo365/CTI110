# Josiah Breckenridge
# 2024-09-27
# P1HW2_BreckenridgeJosiah
# This program calculates travel expenses by subtracting user inputted expenses from a budget.

# Pseudocode:
# 1. Ask the user to enter their budget
# 2. Ask the user to enter their travel destination
# 3. Ask the user for the amount they will spend on gas
# 4. Ask the user for the amount they will spend on accommodation
# 5. Ask the user for the amount they will spend on food
# 6. Calculate the total expenses
# 7. Subtract the expenses from the budget to get the remaining balance
# 8. Display the destination, initial budget, and expenses (gas, accommodation, food)
# 9. Display the remaining balance

# Asking the user for their budget
budget = float(input("Enter Budget: "))

# Asking for the travel destination
destination = input("Enter your travel destination: ")

# Asking for expenses
fuel_cost = float(input("How much do you think you will spend on gas? "))
accommodation_cost = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_cost = float(input("Last, how much do you need for food? "))

# Calculating total expenses
total_expenses = fuel_cost + accommodation_cost + food_cost

# Calculating remaining balance
remaining_balance = budget - total_expenses

# Displaying the results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"\nFuel: {fuel_cost}")
print(f"Accommodation: {accommodation_cost}")
print(f"Food: {food_cost}")
print(f"\nRemaining Balance: {remaining_balance}")
