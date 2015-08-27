# ★ There are 264 distinct words in the Brown Corpus having exactly three possible tags.
# Print a table with the integers 1..10 in one column, and the number of distinct words in the corpus having 1..10 distinct tags in the other column.

# For the word with the greatest number of distinct tags, print out sentences from the corpus containing the word, one for each possible tag.

import nltk
from nltk.corpus import brown
from tabulate import tabulate

tags = brown.tagged_words()
cfd = nltk.ConditionalFreqDist(tags)

num_tags = []
for condition in cfd.conditions():
    num_tags.append((condition, len(cfd[condition])))

tags_by_num = []

for i in range(11):
    this_num = 0
    for (word, num) in num_tags:
        if num == i:
            this_num += 1
    tags_by_num.append((i, this_num))

# prints a table of the integers 1-10 and the numbers of distinct words in the corpus that have those numbers of distinct tags

print(tabulate(tags_by_num))

# "that" is the word with the most distinct tags.
distinct_tags = [tag for tag in cfd['that']]

tagged_sents = brown.tagged_sents()

# go through each sentence in the corpus. 
# go through each tag in the sentence

for sent in tagged_sents:
    for (word, tag) in sent:
        for distinct_tag in distinct_tags:
            if distinct_tag == tag and (word == 'That' or word == 'that'):
                print(sent)
                distinct_tags.remove(distinct_tag)
                print("************")
                break