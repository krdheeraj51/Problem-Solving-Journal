# Prime Number Checker
# Check if a number is prime 
def isPrime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
number = 29 
print(f"{number} is prime: {isPrime(number)}")  # Output: 29 is prime: True
number = 30
print(f"{number} is prime: {isPrime(number)}")  # Output: 30 is prime: False
