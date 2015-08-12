# ◑ Inspect the confusion matrix for the bigram tagger t2 defined in 5, and identify one or more sets of tags to collapse. Define a dictionary to do the mapping, and evaluate the tagger on the simplified data.

#imports 
import nltk
from nltk.corpus import brown

# getting the data ready
brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

# prepping the taggers


def collapse(sentences_to_collapse):
	"""converts according to the conversion dictionary. collapses tags into a single category"""

	conversion_dict = {'NNS': 'NN', 'NN-HL':'NN', 'NN-NC': 'NN', 'NN-TL': 'NN'}
	# produces all the tags for the test data
	new_tagged_sents = []
	
	for sent in sentences_to_collapse:
		new_sent = []
		for word in sent:
			changed = False
			for switch in conversion_dict:
				if word[1] == switch:
					new_sent.append((word[0], conversion_dict[switch]))
					changed = True
			if changed == False:
				new_sent.append(word)
		new_tagged_sents.append(new_sent)
	return new_tagged_sents



t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)

# old value - 0.9606877896453647

print(t2.evaluate(brown_tagged_sents))

train_sents = collapse(train_sents)
brown_tagged_sents = collapse(brown_tagged_sents)

print(t2.evaluate(brown_tagged_sents))





# produces all the golden tags

# test_tags = [tag for sent in brown.sents(categories='editorial') for (word, tag) in t2.tag(sent)]
# gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]

