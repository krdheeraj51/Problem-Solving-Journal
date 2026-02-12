# 2026 Winter Games Day 7: Speed Skating
# Given two arrays representing the lap times (in seconds) for two speed skaters, 
# return the lap number where the difference in lap times is the largest.

# The first element of each array corresponds to lap 1, the second to lap 2, and so on.
# The difference in lap times is calculated as the absolute value of the difference between the two skaters' lap times for that lap.
# Return the lap number (1-indexed) where the difference is the largest. If there are multiple laps with the same largest difference, return the earliest lap number.

def largest_lap_time_difference(skater1_times, skater2_times):
    max_difference = 0
    lap_with_max_difference = 1
    
    for i in range(len(skater1_times)):
        difference = abs(skater1_times[i] - skater2_times[i])
        if difference > max_difference:
            max_difference = difference
            lap_with_max_difference = i + 1  # +1 for 1-indexed lap number
            
    return lap_with_max_difference