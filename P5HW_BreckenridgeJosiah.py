# Josiah Breckenridge
# 2024-11-18
# Math Quiz Program
# This program gives simple math quizzes with a menu-driven interface that allows the user to choose between addition or subtraction problems.

import random

def addition_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    guess_count = 0
    print(f"\n  {num1}\n+ {num2}")
    while True:
        user_answer = int(input("Enter answer: "))
        guess_count += 1
        if user_answer < correct_answer:
            print("Sorry, guess is too low.")
        elif user_answer > correct_answer:
            print("Sorry, guess is too high.")
        else:
            print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {guess_count}\n")
            break

def subtraction_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2
    guess_count = 0
    print(f"\n  {num1}\n- {num2}")
    while True:
        user_answer = int(input("Enter answer: "))
        guess_count += 1
        if user_answer < correct_answer:
            print("Sorry, guess is too low.")
        elif user_answer > correct_answer:
            print("Sorry, guess is too high.")
        else:
            print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {guess_count}\n")
            break

def main():
    while True:
        print("\nMAIN MENU")
        print("--------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        choice = input("Please choose one of the menu options: ")

        if choice == "1":
            addition_quiz()
        elif choice == "2":
            subtraction_quiz()
        elif choice == "3":
            print("Thank you for playing...\nBye!!")
            break
        else:
            print("\nInvalid choice. Please enter a valid menu option (1, 2, or 3).\n")

if __name__ == "__main__":
    main()
