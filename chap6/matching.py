import re
pattern = r'ca+t'
texts = ['cat', 'caat', 'caaaat', 'ct']
for text in texts:
    if re.match(pattern, text):
        print(f"Match found for '{text}'")
    else:
        print(f"No match for '{text}'")
# Output:
# Match found for ’cat’
# Match found for ’caat’
# Match found for ’caaaat’
# No match for ’ct’