# 2026 Winter Games Day 2: Snowboarding
# Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.

# A snowboarder's stance is either "Regular" or "Goofy".
# Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation, and negative indicate counter-clockwise rotation.
# The landing stance flips every 180 degrees of rotation.
# For example, given "Regular" and 90, return "Regular". Given "Regular" and 180 degrees, return "Goofy".


def landing_stance(starting_stance, rotation):
    # Calculate the number of 180-degree flips
    flip = (rotation // 90) % 2  # 0 for even flips, 1 for odd flips
    if flip == 0 and (rotation / 90) > 0:
        return "Goofy" 
    else:
        return "Regular"
    
# Example usage:
print(landing_stance("Regular", 90))   # Output: "Regular"
print(landing_stance("Regular", 180))  # Output: "Goofy"
