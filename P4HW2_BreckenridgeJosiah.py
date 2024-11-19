# Josiah Breckenridge
# Date: MM/DD/YYYY
# P4HW2 - Employee Pay Calculator for Multiple Employees
# A program to calculate the gross pay, overtime, and regular pay for multiple employees, and display the totals.

# Pseudocode:
# 1. Initialize variables to store total overtime, total regular pay, total gross pay, and employee count.
# 2. Start a loop to collect employee information until the user enters "Done".
#    - Ask for the employee's name.
#    - If name is "Done", break the loop.
#    - Ask for hours worked and pay rate.
#    - Calculate overtime and regular pay.
#    - Add values to the total variables.
#    - Display individual employee pay information.
# 3. After exiting the loop, display the total amounts and number of employees.

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Start collecting employee information
while True:
    # Get employee's name or check if user wants to terminate
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break

    # Get hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate regular and overtime pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Add to totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display individual employee pay details
    print("\nEmployee name:", employee_name)
    print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
    print("--------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:.2f}")
    print()

# Display summary
print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
