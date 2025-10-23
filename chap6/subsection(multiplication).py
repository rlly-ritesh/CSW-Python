import re
pattern = r'ca*t'
texts = ['ct', 'cat', 'caat', 'caaaat']
for text in texts:
    if re.match(pattern, text):
        print(f"Match found for '{text}'")

# Output:
# Match found for ’ct’
# Match found for ’cat’
# Match found for ’caat’
# Match found for ’caaaat’