# Cooldown Time
# Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

# Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
# A user must wait at least 48 hours before retaking an exam.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-25
from datetime import datetime, timedelta
def can_take_exam_again(finish_time, current_time):
    finish_dt = datetime.strptime(finish_time, "%Y-%m-%dT%H:%M:%S")
    current_dt = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S")
    
    return (current_dt - finish_dt) >= timedelta(hours=48)

# Test Cases
print(can_take_exam_again("2026-03-25T14:00:00", "2026-03-27T14:00:00"))  # Output: True
print(can_take_exam_again("2026-03-25T14:00:00", "2026-03-27T13:59:59"))  # Output: False