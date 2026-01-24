# Bingo! Letter
# Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:

# Letter	Number Range
# "B"	1-15
# "I"	16-30
# "N"	31-45
# "G"	46-60
# "O"	61-75

def get_bingo_letter(number):
    if 1 <= number <= 15:
        return "B"
    elif 16 <= number <= 30:
        return "I"
    elif 31 <= number <= 45:
        return "N"
    elif 46 <= number <= 60:
        return "G"
    elif 61 <= number <= 75:
        return "O"
    else:
        return "Invalid number"
