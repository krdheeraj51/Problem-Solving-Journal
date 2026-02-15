# 2026 Winter Games Day 10: Alpine Skiing
# Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

# To determine the rating:

# Calculate the steepness of the hill by taking the drop divided by the distance.
# Then, calculate the adjusted steepness based on the hill type:
# "Downhill" multiply steepness by 1.2
# "Slalom": multiply steepness by 0.9
# "Giant Slalom": multiply steepness by 1.0
# Return:

# "Green" if the adjusted steepness is less than or equal to 0.1
# "Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
# "Black" if the adjusted steepness is greater than 0.25

def get_hill_rating(drop, distance, hill_type):
    steepness_of_hill = drop/distance
    adjusted_steepness=0
    if hill_type == "Downhill":
        adjusted_steepness= steepness_of_hill * 1.2   
    elif hill_type == "Slalom":
        adjusted_steepness= steepness_of_hill * 0.9
    elif hill_type == "Giant Slalom":
        adjusted_steepness= steepness_of_hill * 1.0

    if adjusted_steepness <= 0.1:
        return "Green"
    elif adjusted_steepness > 0.1 and adjusted_steepness <= 0.25 :
        return "Blue"
    elif adjusted_steepness > 0.25:
        return "Black"
