import re
pattern = r'\d\d\d-\d\d\d-\d\d\d\a'
text = 123-456-7890
if re.match(pattern, text):
    print ("Number accepted!")
else:
    print ("Incorrect format!")