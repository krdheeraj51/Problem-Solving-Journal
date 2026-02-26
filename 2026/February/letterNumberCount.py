# Letter and Number Count
# Given a string, return a message with the count of how many letters and numbers it contains.

# Letters are A-Z and a-z.
# Numbers are 0-9.
# Ignore all other characters.
# Return "The string has X letters and Y numbers.", where "X" is the count of letters and "Y" is the count of numbers.
# If either count is 1, use the singular form for that item. E.g: "1 letter" instead of "1 letters" and "1 number" instead of "1 numbers".

def count_letters_and_numbers(s):
    letters = 0
    numbers = 0
    
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            numbers += 1
            
    letter_word = "letter" if letters == 1 else "letters"
    number_word = "number" if numbers == 1 else "numbers"
    
    return f"The string has {letters} {letter_word} and {numbers} {number_word}."