# ◑ Write programs to process the Brown Corpus and find answers to the following questions:
# Which tags are nouns most commonly found after? What do these tags represent? - articles or adjectives are the most common. complete
# Which nouns are more common in their plural form, rather than their singular form? (Only consider regular plurals, formed with the -s suffix.) complete
# Which word has the greatest number of distinct tags. What are they, and what do they represent? complete
# List tags in order of decreasing frequency. What do the 20 most frequent tags represent? - complete

from nltk.corpus import brown

import nltk

cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
tags = brown.tagged_words(categories='news')
pos_tags = [val for key, val in tags]

#this represents the tags in decreasing order of frequency.

fd = nltk.FreqDist(pos_tags)
common_tags = fd.most_common(20)

# pulls out all the different words

conditions = cfd.conditions()
number_of_tags = []

# creates a new list with each word followed by the number of distinct tags that it has

for condition in conditions:
	number_of_tags.append((condition, len(cfd[condition])))

# makes a new list that has the words organized in decreasing order by how many tags they have. the answer is 'to' they are TO': 1222, 'IN': 880, 'TO-HL': 6, 'IN-HL': 5, 'IN-TL': 2, 'NPS': 1. it's most commonly used as a preposition

number_of_tags = list(reversed(sorted(number_of_tags, key=lambda x: x[1])))
print(number_of_tags[0:19])

# produces the list of nouns more common in their plural form than in their singular form.
# does this by looking in the frequency distribution for each word and comparing the number of
# hits for plural noun tags and singular tags

for condition in conditions:
	if cfd[condition]['NNS'] > cfd[condition]['NN']:
		print(condition)

# makes bigrams of the tag pairs in the text
word_tag_pairs = nltk.bigrams(tags)
# pulls out all the tags of the words that precede nouns
noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NN']
# makes a frequency distribution
fdist = nltk.FreqDist(noun_preceders)
# pulls out all the most common tags
[tag for (tag, _) in fdist.most_common()]