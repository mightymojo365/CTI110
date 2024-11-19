# Josiah Breckenridge
# 2024-09-27
# P1HW1_BreckenridgeJosiah
# This program calculates the exponentiation of two integers and performs an addition and subtraction operation on three integers provided by the user.

# Calculating Exponents
print("-----Calculating Exponents----")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

# Addition and Subtraction
print("-----Addition and Subtraction----")
start_value = int(input("Enter a starting integer: "))
add_value = int(input("Enter an integer to add: "))
subtract_value = int(input("Enter an integer to subtract: "))
final_result = start_value + add_value - subtract_value
print(f"\n{start_value} + {add_value} - {subtract_value} is equal to {final_result}")
