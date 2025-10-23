import re
pattern = r'ca*t'
texts = ["ct", "cat", "caat", "caaaat"]
for text in texts:
    if re.match(pattern, text):
        print (f"Match found for ’'{text}’")
        