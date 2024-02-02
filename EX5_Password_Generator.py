# This exercise is aimed at practicing regular expressions 

# Notes: 
# A regular expression, or regex, is a pattern used to match a specific combination of characters inside a string. It is a valid alternative to if/else conditional statements when you need to match or find patterns inside a string for validation purposes, character replacement, and others.
# The "re" module allows you to use regular expressions in your code.
# The compile() function from the re module compiles the string passed as the argument into a regular expression object that can be used by other re methods.
# The search() function from the re module analyzes the string passed as the argument looking for the first place where the regex pattern matches the string.
# In your pattern, you can add a quantifier after a character to specify how many times that character should be repeated. For example, the + quantifier means it should repeat one or more times.
# To check that the generated password meets the required features, we use the findall() function from the re module. It's similar to search but it returns a list with all the occurrences of the matched pattern.

# A character class is indicated by square brackets and matches one character among those specified between the brackets. For example, ma[dnt] matches either mad, man, or mat.
# Character classes also allow you to indicate a range of characters to match. You need to specify the starting and the ending characters separated by an hyphen, -. Characters follow the Unicode order. 

# The caret, ^, placed at the beginning of the character class, matches all the characters except those specified in the class [^0-9].
# The dot character is a wildcard that matches any character in a string — except for a newline character by default. 
# The character class \d is a shorthand for [0-9].
# In a character class, you can combine multiple ranges by writing one range after another inside the square brackets (without any additional characters). For example: [a-d3-6] is the combination of [a-d] and [3-6].
# In the same way the [0-9] class is equivalent to \d, the [^0-9] class is equivalent to \D. Alphanumeric characters can be matched with \w and non-alphanumeric characters can be matched with \W.
# Since the underscore character is a valid character for variable names, it is included in the \w character class (equivalent to [a-zA-Z0-9_]), which can be conveniently used to match variable names.
# Therefore, the \W character class is equivalent to [^a-zA-Z0-9_] with the underscore character that is not matched. For this reason you cannot use it to match all your special characters.

# random.random() returns a random floating point number from 0.0 inclusive to 1.0 exclusive.
# random.choice() takes in a sequence and returns a random item from the sequence.

import re
import secrets
import string

# Define the generate password function with default parameters
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        # Define constraints
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)