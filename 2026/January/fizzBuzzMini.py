# FizzBuzz Mini
# Given an integer, return a string based on the following rules:

# If the number is divisible by 3, return "Fizz".
# If the number is divisible by 5, return "Buzz".
# If the number is divisible by both 3 and 5, return "FizzBuzz".
# Otherwise, return the given number as a string.

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
    
# Example usage:
print(fizz_buzz(15))  # Output: "FizzBuzz"