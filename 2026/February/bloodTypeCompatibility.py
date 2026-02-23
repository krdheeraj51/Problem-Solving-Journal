# Blood Type Compatibility
# Given a donor blood type and a recipient blood type, determine whether the donor can give blood to the recipient.

# Each blood type consists of:

# A letter: "A", "B", "AB", or "O"
# And an Rh factor: "+" or "-"
# Blood types will be one of the valid letters followed by an Rh factor. For example, "AB+" and "O-" are valid blood types.

# Letter Rules:

# "O" can donate to other letter type.
# "A" can donate to "A" and "AB".
# "B" can donate to "B" and "AB".
# "AB" can donate only to "AB".
# Rh Rules:

# Negative ("-") can donate to both "-" and "+".
# Positive ("+") can donate only to "+".
# Both letter and Rh rule must pass for a donor to be able to donate to the recipient.
#https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-23

def can_donate(donor, recipient):
    donor_letter, donor_rh = donor[:-1], donor[-1]
    recipient_letter, recipient_rh = recipient[:-1], recipient[-1]

    # Check letter compatibility
    if donor_letter == "O":
        letter_compatible = True
    elif donor_letter == "A":
        letter_compatible = recipient_letter in ["A", "AB"]
    elif donor_letter == "B":
        letter_compatible = recipient_letter in ["B", "AB"]
    elif donor_letter == "AB":
        letter_compatible = recipient_letter == "AB"
    else:
        return False  # Invalid blood type

    # Check Rh compatibility
    if donor_rh == "-":
        rh_compatible = True
    elif donor_rh == "+":
        rh_compatible = recipient_rh == "+"
    else:
        return False  # Invalid blood type

    return letter_compatible and rh_compatible

print(can_donate("O-", "A+"))  # True
print(can_donate("A+", "AB+"))  # True