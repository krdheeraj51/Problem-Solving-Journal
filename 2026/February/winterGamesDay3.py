# 2026 Winter Games Day 3: Biathlon
# Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.

# Each round consists of 5 targets.
# Each missed target results in a 150 meter penalty loop.

def biathlon_penalty(rounds):
    total_penalty = 0
    for hits in rounds:
        missed_targets = 5 - hits
        total_penalty += missed_targets * 150
    return total_penalty

# Example usage:
rounds = [5, 4, 3, 5, 2]
print(biathlon_penalty(rounds))  # Output: 900