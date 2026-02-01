# Letters-Numbers
# Given a string containing only letters and numbers, return a new string where a hyphen (-) 
# is inserted every time the string switches from a letter to a number, or a number to a letter.

def letter_number_separator(s):
    if not s:
        return s
    
    result = [s[0]]
    
    for i in range(1, len(s)):
        if (s[i].isalpha() and s[i-1].isdigit()) or (s[i].isdigit() and s[i-1].isalpha()):
            result.append('-')
        result.append(s[i])
    
    return ''.join(result)

# Example usage:
input_string = "abc123def456"   
output_string = letter_number_separator(input_string)
print(output_string)  # Output: "abc-123-def-456"

# Learning Points:
# 1. String Traversal: The function iterates through the string starting from the second character to compare each character with the previous one.
# 2. Character Type Checking: The isalpha() and isdigit() methods are used to determine whether a character is a letter or a number.
# 3. List for Efficient String Building: A list is used to build the result string  
#    efficiently, as string concatenation in a loop can be costly in terms of performance.
# 4. Joining List into String: The join() method is used to convert the list of characters back into a single string at the end.    
