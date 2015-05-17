# 11. Create a list of words and store it in a variable sent1. Now assign sent2 = sent1. Modify one of the items in
# sent1 and verify that sent2 has changed.
# 1. Now try the same exercise but instead assign sent2 = sent1[:]. Modify sent1 again and see what happens to
# sent2. Explain.
# 2. Now define text1 to be a list of lists of strings (e.g. to represent a text consisting of multiple sentences. Now
# assign text2 = text1[:], assign a new value to one of the words, e.g. text1[1][1] = 'Monty'. Check what
# this did to text2. Explain.
# 3. Load Python's deepcopy() function (i.e. from copy import deepcopy), consult its documentation, and test that
# it makes a fresh copy of any object.

from copy import deepcopy

sent1 = ['this', 'is', 'my', 'list', 'of', 'words']
sent2 = sent1[:]
sent1[0] = 'BOO'
print(sent2)

# 11.1 does that because it's copying the object references inside the list. not the object reference to the list itself. so the original object reference remains intact even if the list gets overwritten.

text1 = [['this', 'is', 'my', 'first', 'sentence.'], ['this', 'is', 'sentence', 'two'], ['sentence', 'three', 'punk.']]
print(text1)
text2 = deepcopy(text1)
text1[1][1]= 'foot'
print(text1)
print(text2)

# this still affected text 2 because it is referencing a structured element. So even though you copy the object references, that object reference is itself to an object reference, which got overwritten