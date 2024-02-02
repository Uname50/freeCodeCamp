# This exercise is aimed at practicing list comprehensions by building a case converter program

def convert_to_snake_case(pascal_or_camel_cased_string):

# longer version of the code that has the same functionality as the list comprehension below:
# snake_cased_char_list = []
# for char in pascal_or_camel_cased_string:
#     if char.isupper():
#         converted_character = '_' + char.lower()
#         snake_cased_char_list.append(converted_character)
#     else:
#         snake_cased_char_list.append(char)
    
# By the end of the loop, snake_cased_char_list should contain all the converted characters in correct order. Use the .join() string method to convert the list of characters into a string.
# ''.join(snake_cased_char_list)
# This joins the characters from the list to the empty string on which you called the .join() method. Save the result in a variable named snake_cased_string on the same level as the snake_cased_char_list variable.
# snake_cased_string = ''.join(snake_cased_char_list)
    
# The easiest way to strip unwanted characters is by using the .strip() string method and passing what to strip to the method as argument.
# clean_snake_cased_string = snake_cased_string.strip('_')

# return clean_snake_cased_string

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('HelloWorldInWeirdCase'))

if __name__ == '__main__':
    main()