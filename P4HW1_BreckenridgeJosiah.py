# Josiah Breckenridge
# Date: MM/DD/YYYY
# P4HW1 - Score Average Program with Grade
# A program that collects user scores, validates inputs, calculates average after dropping the lowest score, and assigns a letter grade.

# Pseudocode:
# 1. Ask user how many scores they want to enter.
# 2. Create a loop to collect the scores.
#    - Validate each score to ensure it's between 0 and 100.
#    - If invalid, notify user and prompt for a valid score.
#    - Add valid scores to a list.
# 3. After collecting scores:
#    - Find the lowest score and remove it from the list.
#    - Calculate the average of the modified list.
#    - Determine the letter grade based on the average.
# 4. Display the lowest score, modified list, average, and letter grade.

# Ask for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Initialize an empty list for scores
scores = []

# Collect scores with validation
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i + 1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i + 1} again: ", end="")

# Find the lowest score
lowest_score = min(scores)
# Create a modified list without the lowest score
modified_scores = scores.copy()
modified_scores.remove(lowest_score)

# Calculate the average of the modified list
average_score = sum(modified_scores) / len(modified_scores)

# Determine the letter grade based on average
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {grade}")
print("-------------------------------")
