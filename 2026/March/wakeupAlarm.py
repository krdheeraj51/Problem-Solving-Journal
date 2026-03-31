# Wake-Up Alarm
# Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.

# Both times will be given in "HH:MM" 24-hour format.
# Return:

# "early" if you woke up before your alarm time.
# "on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
# "late" if you woke up more than 10 minutes after your alarm time.
# Both times are on the same day.

def wakeup_alarm(alarm_time, wake_time):
    # Convert time strings to minutes
    def time_to_minutes(t):
        hours, minutes = map(int, t.split(':'))
        return hours * 60 + minutes
    
    alarm_minutes = time_to_minutes(alarm_time)
    wake_minutes = time_to_minutes(wake_time)
    
    if wake_minutes < alarm_minutes:
        return "early"
    elif wake_minutes <= alarm_minutes + 10:
        return "on time"
    else:
        return "late"