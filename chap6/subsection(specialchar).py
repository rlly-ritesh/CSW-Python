import re
pattern = r'ca\+t'
text = 'ca+t'
if re.match(pattern, text):
    print("Match found!")
else:
    print("No match!")
# Output: Match found!