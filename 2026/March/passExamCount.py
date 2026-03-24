# Passing Exam Count
# Given an array of student exam scores and the score needed to pass it,
#  return the number of students that passed the exam.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-24

def pass_exam_count(scores, pass_score):
    count = 0
    for score in scores:
        if score >= pass_score:
            count += 1
    return count

print(pass_exam_count([85, 90, 78, 92, 88], 80))  # Output: 4
print(pass_exam_count([60, 70, 75, 80, 85], 75))  # Output: 3