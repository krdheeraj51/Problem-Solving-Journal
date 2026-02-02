#                   Groundhog Day
# Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.

# Given a value representing the groundhog's appearance, return the correct prediction:

# If the given value is the boolean true (the groundhog saw its shadow), return "Looks like we'll have six more weeks of winter.".
# If the value is the boolean false (the groundhog did not see its shadow), return "It's going to be an early spring.".
# If the value is anything else (the groundhog did not show up), return "No prediction this year.".

def groundhog_day(appearance):
    if appearance is True:
        return "Looks like we'll have six more weeks of winter."
    elif appearance is False:
        return "It's going to be an early spring."
    else:
        return "No prediction this year."

print(groundhog_day(True))   # Looks like we'll have six more weeks of winter.
print(groundhog_day("False"))  # It's going to be an early spring.