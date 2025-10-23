import re
def extract_unique_digits(expression):
    # Step 1: Create an empty list to store digits
    digits = []
    # Step 2: Go through each character in the expression
    for char in expression:
        # Step 3: Check if the character is a digit (0-9)
        if char.isdigit():
            # Step 4: Add it to the list if it's not already there
            if char not in digits:
                digits.append(char)
    # Step 5: Sort the digits in descending order
    digits.sort(reverse=True)
    # Step 6: Convert each digit from string to integer
    result = [int(d) for d in digits]
    # Step 7: Return the final list
    return result
# Example usage
print(extract_unique_digits("2+3*4"))  # Output: [4, 3, 2]
