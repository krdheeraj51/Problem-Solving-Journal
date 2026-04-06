# What Day Is It?
# Given a Unix timestamp in milliseconds, return the day of the week.

# Valid return days are:

# "Sunday"
# "Monday"
# "Tuesday"
# "Wednesday"
# "Thursday"
# "Friday"
# "Saturday"
# Be sure to ignore time zones.
# The method "utcfromtimestamp" in class "datetime" is deprecated
#   Use timezone-aware objects to represent datetimes in UTC; e.g. by calling .fromtimestamp(datetime.timezone.utc)

from datetime import datetime,timezone 
def get_day_of_week(timestamp):
    # Convert the timestamp from milliseconds to seconds
    timestamp_seconds = timestamp / 1000
    
    # Get the day of the week using the datetime module
    day_of_week = datetime.fromtimestamp(timestamp_seconds, tz=timezone.utc).strftime('%A')
    print(f"Timestamp: {timestamp}, Day of Week: {day_of_week}")
    
    return day_of_week

print(get_day_of_week(1614556800000))  # Output: "Monday"