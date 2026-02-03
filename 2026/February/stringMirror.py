# String Mirror
# Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.

def string_mirror(s):
    return s + s[::-1]  

print(string_mirror("abc"))      # "abccba"
print(string_mirror("hello"))    # "helloolleh"
print(string_mirror("12345"))    # "1234554321"