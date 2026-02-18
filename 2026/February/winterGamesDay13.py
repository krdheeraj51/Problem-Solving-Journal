# 2026 Winter Games Day 13: Nordic Combined
# Given an array of jump scores for athletes, calculate their start delay times for the cross-country portion of 
# the Nordic Combined.

# The athlete with the highest jump score starts first (0 second delay). All other athletes start later 
# based on how far behind their jump score is compared to the best jump.

# To calculate the delay for each athlete, subtract the athlete's jump score from the best overall 
# jump score and multiply the result by 1.5. 
# Round the delay up to the nearest integer.
import math
def calculate_start_delays(jump_scores):
    best_score = max(jump_scores)
    delays = []
    
    for score in jump_scores:
        delay = math.ceil((best_score - score) * 1.5)
        delays.append(delay)
    
    return delays