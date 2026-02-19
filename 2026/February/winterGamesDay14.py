# 2026 Winter Games Day 14: Ski Mountaineering
# Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

# The snow depth values are "Shallow", "Moderate", or "Deep".
# Slope values are "Gentle", "Steep", or "Very Steep".
# Return "Safe" or "Risky" based on this table:

# "Shallow"	"Moderate"	"Deep"
# "Gentle"	"Safe"	"Safe"	"Safe"
# "Steep"	"Safe"	"Risky"	"Risky"
# "Very Steep"	"Safe"	"Risky"	"Risky"
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-19
def avalanche_risk(snow_depth, slope):
    if snow_depth == "Shallow":
        return "Safe"
    elif snow_depth == "Moderate":
        if slope == "Gentle":
            return "Safe"
        else:
            return "Risky"
    elif snow_depth == "Deep":
        if slope == "Gentle":
            return "Safe"
        else:
            return "Risky"