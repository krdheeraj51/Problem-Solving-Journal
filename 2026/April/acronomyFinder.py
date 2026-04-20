# Acronym Finder
# Given a string representing an acronym, return the full name of the 
# organization it belongs to from the list below:

# "National Avocado Storage Authority"
# "Cats Infiltration Agency"
# "Fluffy Beanbag Inspectors"
# "Department Of Jelly"
# "Wild Honey Organization"
# "Eating Pancakes Administration"
# Each letter in the given acronym should match the 
# first letter of each word in the organization it belongs to, in the same order.

def acronym_finder(acronym):
    organizations = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ]
    
    for org in organizations:
        words = org.split()
        if len(words) == len(acronym):
            if all(word[0] == acronym[i] for i, word in enumerate(words)):
                return org
    
    return "Acronym not found in the list of organizations."