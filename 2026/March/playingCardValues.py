# Playing Card Values
# Given an array of playing cards, return a new array with the numeric value of each card.

# Card Values:

# An Ace ("A") has a value of 1.
# Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
# Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
# Suits:

# Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
# Card Format:

# Each card is represented as a string: "valueSuit". 
# For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.

def card_values(cards):
    values = []
    for card in cards:
        value = card[:-1]  # Get the value part of the card (excluding the suit)
        if value == "A":
            values.append(1)
        elif value in ["J", "Q", "K"]:
            values.append(10)
        else:
            values.append(int(value))  # Convert numbered cards to integers
    return values

print(card_values(["AS", "10H", "QC"]))  # Output: [1, 10, 10]
print(card_values(["2D", "3C", "4S", "5H"]))  # Output: [2, 3, 4, 5]
print(card_values(["JH", "KD", "QS", "AC"]))  # Output: [10, 10, 10, 1]
