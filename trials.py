"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    odd_indices = []

    for i in range(len(items)):
        if items[i] % 2 != 0:
            odd_indices.append(i)

    # for item in items:
    #     if item % 2 != 0:
    #         odd_indices.append(items.index(item))

    return odd_indices


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f"${i}. ${item}")

    i += 1 


def get_range(start, stop):
    nums = []
    num = start 
    while num < stop:
        nums.append(num)
        num += 1


def censor_vowels(word):
    chars = []
    vowels = "aeiou"

    for letter in word:
        if letter in vowels:
            chars.append("*")
        else:
            chars.append(letter)
    
    return "".join(chars)


def snake_to_camel(string):
    camelCase = []

    for word in string.split(" "):
        camelCase.append(f"{word[0].upper()}{word[1:]}")

    return camelCase.join("")


def longest_word_length(words):
    longest = words[0]

    for word in words:
        if longest < len(word):
            longest = word 
    
    return longest 


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return result.join("")


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        
    if parens > 0:
        return False 
        
    elif parens == 0:
        return True
    

def compress(string):
    compressed = []

    current_char = ""
    char_count = 0

    for char in string:
        if char != current_char:
            compressed.append(current_char)
    
            if char_count > 1:
                compressed.append(str(char_count))

            current_char = char
            char_count = 0

        char_count += 1

    compressed.append(current_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return compressed.join("")

