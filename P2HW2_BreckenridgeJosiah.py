# Josiah Breckenridge
# Date: 10/11/2024
# Assignment: P2HW2_GradeCalculator
# This program asks the user to enter grades for six modules, stores them in a list,
# and then displays the lowest, highest, sum of the grades, and the average.

# Pseudocode:
# 1. Prompt the user to enter grades for six modules.
# 2. Store the grades in a list.
# 3. Calculate the lowest grade.
# 4. Calculate the highest grade.
# 5. Calculate the sum of the grades.
# 6. Calculate the average of the grades.
# 7. Display the lowest, highest, sum, and average with proper formatting.

# Collect grades from the user
grades = []  # Create an empty list to store grades
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Perform calculations
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# Display the results
print("\n------------Results------------")
print(f"{'Lowest Grade:':<15} {lowest_grade:.1f}")
print(f"{'Highest Grade:':<15} {highest_grade:.1f}")
print(f"{'Sum of Grades:':<15} {sum_of_grades:.1f}")
print(f"{'Average:':<15} {average_grade:.2f}")
print("-------------------------------")
