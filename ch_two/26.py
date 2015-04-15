import nltk
from nltk.corpus import wordnet as wn

all_noun_synsets = list(wn.all_synsets('n'))

# for item in all_noun_synsets:
# 	item = item.lower()
hyponym_count = 0
synset_count = 0

for item in all_noun_synsets:
	if item.hyponyms():
		hyponym_count += len(item.hyponyms())
		synset_count += 1

print(hyponym_count)
print(synset_count)
average_hyponym_branching = hyponym_count / synset_count
print(average_hyponym_branching)
# all_noun_synsets = all_noun_synsets.lower()
# 	for syn in all_noun_synsets:
