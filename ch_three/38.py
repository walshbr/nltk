# ★ An interesting challenge for tokenization is words that have been split across a line-break. E.g. if long-term is split, then we have the string long-\nterm.

# Write a regular expression that identifies words that are hyphenated at a line-break. The expression will need to include the \n character.
# Use re.sub() to remove the \n character from these words.
# How might you identify words that should not remain hyphenated once the newline is removed, e.g. 'encyclo-\npedia'?x


import re

pattern = re.compile(r'[a-zA-Z]+/n[a-zA-Z]+')

pattern.sub(' ', text)

# i would put that it in a function with a branch. It looks up the hyphenated word in the dictionary. If it successfully finds the word in the dictionary, it keeps the line-break. It would maybe just have to look up each individual section, since you're basically looking for hyphenated phrases. So it would look to make sure both words were in the dictionary.