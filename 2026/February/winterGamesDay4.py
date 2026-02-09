# 2026 Winter Games Day 4: Ski Jumping
# Given distance points, style points, a wind compensation value, and K-point bonus value, calculate your score for the ski jump and determine if you won a medal or not.

# Your score is calculated by summing the above four values.
# The current total scores of the other jumpers are:

# 165.5
# 172.0
# 158.0
# 180.0
# 169.5
# 175.0
# 162.0
# 170.0
# If your score is the best, return "Gold"
# If it's second best, return "Silver"
# If it's third best, return "Bronze"
# Otherwise, return "No Medal"

def ski_jump_score(distance_points, style_points, wind_compensation, k_point_bonus):
    score = distance_points + style_points + wind_compensation + k_point_bonus
    other_scores = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
    
    if score > max(other_scores):
        return "Gold"
    elif score > sorted(other_scores)[-2]:
        return "Silver"
    elif score > sorted(other_scores)[-3]:
        return "Bronze"
    else:
        return "No Medal"
    
# Example usage:
distance_points = 120.0
style_points = 50.0
wind_compensation = 10.0    
k_point_bonus = 20.0
print(ski_jump_score(distance_points, style_points, wind_compensation, k_point_bonus))  # Output: "Silver"

# Learning in this challenge:
  # - we can learn few things 
    # - how to second second and third highest value in a list using sorted() function
    # eg . sorted(other_scores)[-2] will give us the second highest value in the list other_scores
    # - how to compare a value with the maximum value in a list using max() function
