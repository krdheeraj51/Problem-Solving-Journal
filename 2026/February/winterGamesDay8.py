# 2026 Winter Games Day 8: Luge
# Given an array of five numbers, each representing the time (in seconds) 
# it took a luger to complete a segment of a track, determine which segment had the 
# fastest speed and what that speed was.

# The track is divided into the following segments:

# Segment 1: 320 meters
# Segment 2: 280 meters
# Segment 3: 350 meters
# Segment 4: 300 meters
# Segment 5: 250 meters
# The first value in the given array corresponds to the time for segment 1, 
# the second value to segment 2, and so on.

# To calculate the speed (in meters per second) for a segment, divide the distance by the time.

# Return "The luger's fastest speed was X m/s on segment Y.". Where X is the fastest speed, 
# rounded to two decimal places, and Y is the segment number where the fastest speed occurred.

def fastest_luge_speed(times):
    segments = [320, 280, 350, 300, 250]
    fastest_speed = 0
    fastest_segment = 1
    
    for i in range(len(times)):
        speed = segments[i] / times[i]
        if speed > fastest_speed:
            fastest_speed = speed
            fastest_segment = i + 1  # +1 for 1-indexed segment number
            
    return f"The luger's fastest speed was {fastest_speed:.2f} m/s on segment {fastest_segment}."

# Example usage:
times = [40.0, 35.0, 45.0, 30.0, 25.0]
print(fastest_luge_speed(times))  # Output: "The luger's fastest speed