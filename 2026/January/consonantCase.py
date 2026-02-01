# Consonant Case
# Given a string representing a variable name, convert it to consonant case using the following rules:

# All consonants should be converted to uppercase.
# All vowels (a, e, i, o, u in any case) should be converted to lowercase.
# All hyphens (-) should be converted to underscores (_).

def consonant_case(variable_name):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in variable_name:
        if char in vowels:
            result += char.lower()
        elif char == '-':
            result += '_'
        else:
            result += char.upper()
    
    return result
# Example usage:
variable_name = "my-Variable-Name"
print(consonant_case(variable_name))  # Output: "MY_vARIABLE_NAmE"