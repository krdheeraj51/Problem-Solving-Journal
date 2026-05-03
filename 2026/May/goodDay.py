# Good Day
# Given a time string in "HH:MM" format (24-hour clock), return:

# "Good morning" for times 05:00 to 11:59
# "Good afternoon" for times 12:00 to 17:59
# "Good evening" for times 18:00 to 21:59
# "Good night" for times 22:00 to 04:59

def good_day(time_str):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    print(f"Parsed time: {hours} hours and {minutes} minutes")  # Debugging statement
    
    # Determine the appropriate greeting based on the time
    if 5 <= hours < 12:
        return "Good morning"
    elif 12 <= hours < 18:
        return "Good afternoon"
    elif 18 <= hours < 22:
        return "Good evening"
    else:
        return "Good night" 
    