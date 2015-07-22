# 20. Write code to search the Brown Corpus for particular words and phrases according to tags, to answer the following
# questions:
# 1. Produce an alphabetically sorted list of the distinct words tagged as MD.
#complete

# 2. Identify words that can be plural nouns or third person singular verbs (e.g. deals, flies).

# complete

# 3. Identify three-word prepositional phrases of the form IN + DET + NN (eg. in the lab).

# HERE

# 4. What is the ratio of masculine to feminine pronouns

# complete

from nltk.corpus import brown
import nltk

# text = brown.words()
# tagged_text = brown.tagged_words()
# set_text = set(text)
# cfd = nltk.ConditionalFreqDist(tagged_text)
# conditions = cfd.conditions()

# # produces the alphabetically sorted list of distinct words tagged as MD.

# md_words = [condition for condition in conditions if cfd[condition]['MD'] != 0]
# md_words.sort()

# print(md_words)

# # question two - 2. Identify words that can be plural nouns or third person singular verbs (e.g. deals, flies).

# two_words = [condition for condition in conditions if cfd[condition]['NNS'] and cfd[condition]['VBZ']]
# two_words.sort()
# print(two_words)

# # question four

# fd = nltk.FreqDist(text)
# masc_fem_proportion = (fd['he'] + fd['He']) / (fd['she'] + fd['She'])
# print(masc_fem_proportion)

# 3. Identify three-word prepositional phrases of the form IN + DET + NN (eg. in the lab).

# pulls out trigrams for the tagged text
tagged_text = brown.tagged_words()
trigrams = list(nltk.trigrams(tagged_text))
for trigram in trigrams:
	zipped_tag = [t for t in zip(*trigram)]
	if zipped_tag[1] == ('IN', 'DT', 'NN'):
		print(zipped_tag[0])

# note - this is the idea. but there must not be three word phrases of the sort that they are talking about. It works for other combinations but not for those three.


