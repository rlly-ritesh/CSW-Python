# 5. Character Frequency Counter
# Count character frequency in a string and print in order.
def char_frequency():
    text = input("Enter a string: ")
    frequency = {}
    
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()  # Case insensitive
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    
    # Sort by character
    sorted_frequency = dict(sorted(frequency.items()))
    
    for char, freq in sorted_frequency.items():
        print(f"'{char}': {freq}")
    return sorted_frequency
char_frequency()