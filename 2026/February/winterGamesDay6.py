# 2026 Winter Games Day 6: Figure Skating
# Given an array of judge scores and optional penalties, calculate the final score for a figure 
# skating routine.

# The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove 
# the highest and lowest judge scores 
# and sum the remaining 8 scores to get the base score.

# Any additional arguments passed to the function are penalties. Subtract all penalties 
# from the base score to get the final score.

def figure_skating_score(judge_scores, *penalties):
    if len(judge_scores) != 10:
        raise ValueError("There must be exactly 10 judge scores.")
    
    sorted_scores = sorted(judge_scores)
    base_score = sum(sorted_scores[1:-1])  # Remove the highest and lowest scores
    
    total_penalties = sum(penalties)
    final_score = base_score - total_penalties
    
    return final_score