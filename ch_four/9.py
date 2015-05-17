# 9. ☼ Write code that removes whitespace at the beginning and end of a string, and normalizes whitespace between words
# to be a single space character.
# 1. do this task using split() and join()
# 2. do this task using regular expression substitutions

import re

sent = ' this is my sentence that starts and ends with whitespace '
sent = sent.split(' ')

#cleans out all the whitespace

sent = [word for word in sent if word]
sent = ' '.join(sent)
print(sent)

# answer for two that works
sent = ' this is my sentence that starts and ends with whitespace '
pattern = re.compile('^\s|\s$')
sent = pattern.sub('', sent)
print(sent)