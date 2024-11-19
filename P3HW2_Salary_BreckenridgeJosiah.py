# Josiah Breckenridge
# Date: MM/DD/YYYY
# Assignment Name: P3HW2_Salary Calculation
# A brief description of the project: This program calculates the gross pay of an employee based on regular and overtime hours worked.

# Prompt user for input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Initialize regular and overtime pay variables
overtime_hours = 0
overtime_pay = 0

# Determine if there are overtime hours
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    regular_hours = hours_worked

# Calculate regular and overtime pay
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * 1.5

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results with formatted output
print("\n------------------------------------------")
print(f"Employee name:\t{employee_name}")
print("------------------------------------------")
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
print("--------------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:.2f}")
