# Unique Stair Climber
# Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time.

def get_unique_climbs(steps):
    if steps <= 0:
        return 0
    elif steps == 1:
        return 1
    elif steps == 2:
        return 2
    else:
        return get_unique_climbs(steps - 1) + get_unique_climbs(steps - 2)

# Test cases
print(get_unique_climbs(1))  # Output: 1
print(get_unique_climbs(2))  # Output: 2
print(get_unique_climbs(3))  # Output: 3
print(get_unique_climbs(4))  # Output: 5  