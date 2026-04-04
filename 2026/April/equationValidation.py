# Equation Validation
# Given a string representing a math equation, determine whether it is correct.

# The left side may contain up to three positive integers and the operators +, -, *, and /.
# The equation will be given in the format: "number operator number = number" 
# (with two or three numbers on the left). 
# For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
# The right side will always be a single integer.
# Follow standard order of operations: multiplication and division are evaluated before 
# addition and subtraction, from left-to-right.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-04

def equationValidation(equation):
    left_side, right_side = equation.split('=')
    right_value = int(right_side.strip())
    print(f"Left side: '{left_side.strip()}', Right side: {right_value}")

    
    # Evaluate the left side using eval after replacing the operators with their Python equivalents
    left_side = left_side.replace(' ', '')  # Remove spaces
    left_side = left_side.replace('*', '*').replace('/', '/').replace('+', '+').replace('-', '-')
    print(f"Evaluating left side: '{left_side}'")
    try:
        left_value = eval(left_side)
        print(f"Evaluated left value: {left_value}")
        return left_value == right_value
    except Exception as e:
        print(f"Error evaluating equation: {e}")
        return False
    
print(equationValidation("2 + 2 = 4"))  # Output: True
print(equationValidation("2 + 3 - 1 = 4"))  # Output: True
print(equationValidation("2 * 3 + 4 = 10"))  # Output: True
print(equationValidation("10 / 2 - 3 = 2"))  # Output: True
