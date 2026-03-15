# Captured Chess Pieces
# Given an array of strings representing chess pieces you still have on the board, 
# calculate the value of the pieces your opponent has captured.

# In chess, you start with 16 pieces:

# Piece	Abbreviation	Quantity	Value
# Pawn	"P"	8	1
# Rook	"R"	2	5
# Knight	"N"	2	3
# Bishop	"B"	2	3
# Queen	"Q"	1	9
# King	"K"	1	0
# The given array will only contain the abbreviations above.
# Any of the 16 pieces not included in the given array have been captured.
# Return the total value of all captured pieces, unless...
# If the King has been captured, return "Checkmate".

def get_captured_value(pieces):
    # Define the value of each piece
    pice_start ={
        "P": 8,
        "R": 2,
        "N": 2,
        "B": 2,
        "Q": 1,
        "K": 1 
    }
    piece_values = {
        "P": 1,
        "R": 5,
        "N": 3,
        "B": 3,
        "Q": 9,
        "K": 0
    }

    current={}
    for p in pieces:
        current[p] = current.get(p,0)+1
    
    total = 0
    for p in pice_start:
        misssing = pice_start[p] - current.get(p,0)
        if p == "K" and misssing > 0:
            return "Checkmate"
        total += misssing * piece_values[p]
    return total

print(get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]))
print(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]))
# print(get_captured_value(["P", "P", "P", "P", "P", "P", "P", "P", "R", "R", "N", "N", "B", "B", "Q"]))  # Output: 0
# print(get_captured_value(["P", "P", "P", "P", "P", "P", "P", "R", "R", "N", "N", "B", "B", "Q"]))  # Output: 1