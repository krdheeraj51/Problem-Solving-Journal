# Odd or Even Day
# Given a timestamp (number of milliseconds since the Unix epoch), return:

# "odd" if the day of the month for that timestamp is odd.
# "even" if the day of the month for that timestamp is even.
# For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.

from datetime import datetime,timezone

def odd_or_even_day(timestamp):
    date = datetime.fromtimestamp(timestamp / 1000,tz=timezone.utc)
    day = date.day
    return "odd" if day % 2 != 0 else "even"

# Example usage:
timestamp = 1769472000000  # January 27th, 2026
print(odd_or_even_day(timestamp))  # Output: "odd"