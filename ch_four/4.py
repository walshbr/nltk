# ☼ Create a list words = ['is', 'NLP', 'fun', '?']. Use a series of assignment statements (e.g. words[1] =
# words[2]) and a temporary variable tmp to transform this list into the list ['NLP', 'is', 'fun', '!']. Now do the
# same transformation using tuple assignment.

words = ['is', 'NLP', 'fun', '?']

tmp = words[1]
words[1] = words[0]
words[0] = tmp
words[3] = '!'
print(words)

# is is just asking me to do this?

words = tuple(words)

# But how can I reassign elements of a tuple? Can't I…not? because it's immutable? Is there a way to assign a tuple? There's no way to reassign a tuple, right? Should I just be constructing a new tuple out of elements of the old one? Like this?

words = ['is', 'NLP', 'fun', '?']
words = tuple(words)
print(words)
words = words[1] + ' ' + words[0] + ' ' + words[2] + '!' 
print(words)

# but that's not right because it's a string.