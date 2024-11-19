# Josiah Breckenridge
# Date: MM/DD/YYYY
# P4LAB2 - Multiplication Table Program
# A program that displays the multiplication table for a given integer from 1 to 12

# Start the main while loop to repeat the program if needed
while True:
    # Ask the user to enter an integer
    num = int(input("Enter an integer: "))
    
    # Check if the entered integer is non-negative
    if num >= 0:
        # Display multiplication table using a for loop
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")
    else:
        # Inform the user that negative numbers are not accepted
        print("This program does not handle negative numbers.")

    # Ask if the user wants to run the program again
    run_again = input("\nWould you like to run the program again? (yes/no): ").strip().lower()
    
    # If user types 'no', exit the loop and end the program
    if run_again != "yes":
        print("\nExiting program...")
        break
