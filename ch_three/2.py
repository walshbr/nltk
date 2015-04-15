# ☼ We can use the slice notation to remove 
# morphological endings on words. For example,
#  'dogs'[:-1] removes the last character of dogs, 
#  leaving dog. Use slice notation to remove the affixes
#   from these words (we've inserted a hyphen to indicate
#    the affix boundary, but omit this from your strings)
#   : dish-es, run-ning, nation-ality, un-do, pre-heat.

word_1 = 'dishes'
word_2 = 'running'
word_3 = 'nationality'
word_4 = 'undo'
word_5 = 'preheat'

print(word_1[:-2])
print(word_2[:-4])
print(word_3[:-5])
print(word_4[:-2])
print(word_5[:-4])
