def isPrimeNumber(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


print(isPrimeNumber(2))  # True
print(isPrimeNumber(3))  # True
print(isPrimeNumber(4))  # False