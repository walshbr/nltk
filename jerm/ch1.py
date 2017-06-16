# note - not meant to be run. these are all answers as interpreter commands to go with ch1 of the nltk book.

# 15
sorted([word for word in text5 if word.startswith('b')])
# 17
text9[621:644]

# 18
sorted(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8))

# 19

"""first line gets all words, lowercases them, then gets only the types, then sorts them. second line gets all the types, lowers them, then sorts them. second one will be larger, because it's finding types before you lowercase them. so you'll have The and the as distinct word types and then when you lowercase you'll have some duplicate words"""

# 20 - none functionally, but one is checking with a conditional while the other calls a function that probably does the same.

# 21

text2[-2:]

# 22

FreqDist([w for w in text5 if len(w) > 4]).keys()

# 23

for w in text6:
    if w.isupper():
        print(w)

# 24
[w for w in text6 if wendswith('ize')]
[w for w in text6 if 'z' in w]
[w for w in text6 if 'pt' in w]
[w for w in text6 if w.istitle()]

# 25

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

[print(w) for w in sent if w.startswith('sh')]
[print(w) for w in sent if len(w) > 4]

# 26
"""adds together all the lengths of the words in a text"""

sum(len(w) for w in text1) / len(text1)

def vocab_size(text):
    return len(text)

def percent(word, text):
    fd = FreqDist(test)
    return fd[word] / fd.N()

# 29 - is used to compare the two vocabulary sizes - useful if you want to do comparisons across texts.
