# A single determiner (assume that a, an, and the are the only determiners).
# An arithmetic expression using integers, addition, and multiplication, such as 2*3+8.

nltk.re_show('(?x)\b(an?|the)\b', 'an a the look at the an a this is my sentence and it has numbers 1+2+5 2*3+8')

nltk.re_show('\d[\-\+\*]\d[\-\+\*]\d', 'this is my sentence and it has numbers 1+2+5 2*3+8')

# ask eric about line 4 - which seems good except it's pulling in the white space as well. 
# Also it doesn't seem to 
# 