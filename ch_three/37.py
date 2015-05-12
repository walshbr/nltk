# ◑ Read about the re.sub() function for string substitution using regular expressions, using help(re.sub) and by consulting the further readings for this chapter. Use re.sub in writing code to remove HTML tags from an HTML file, and to normalize whitespace.

import re

#opens a file

f = open('file.html')
raw = f.read()

#sets a pattern for stripping out tags
pattern = re.compile(r'<[^>]+>')

#strips them
processed_text = pattern.sub('', raw)

#sets a new pattern for normalizing whitespace.
pattern = re.compile(r'\s')

processed_text = pattern.sub(' ', processed_text)

print(processed_text)