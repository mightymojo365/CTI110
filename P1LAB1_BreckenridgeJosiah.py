Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Josiah Breckenridge
... # 09/18/2024
... # P1LAB1: Welcome Program
... # This program takes the user's first and last names as input
... # and displays a welcome message with their full name.
... 
... # Prompt the user for their first and last name
... first_name = input("Enter your first name: ")
... print(f"First name entered: {first_name}")
... 
... last_name = input("Enter your last name: ")
... print(f"Last name entered: {last_name}")
... 
... # Check if inputs are empty
... if not first_name or not last_name:
...     print("Error: First or last name cannot be empty.")
... else:
...     # Display the welcome message
...     print(f"Hello, {first_name} {last_name}! Welcome to CTI-110.")
... 
SyntaxError: multiple statements found while compiling a single statement
>>> 
======== RESTART: C:/Users/Owner/Downloads/P1LAB1_BreckenridgeJosiah.py ========
Enter your first name: Josiah
First name entered: Josiah
Enter your last name: Breckenridge
Last name entered: Breckenridge
Hello, Josiah Breckenridge! Welcome to CTI-110.
