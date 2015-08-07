# ◑ How serious is the sparse data problem? Investigate the performance of n-gram taggers as n increases from 1 to 6. Tabulate the accuracy score. 
#complete


# Estimate the training data required for these taggers, assuming a vocabulary size of 105 and a tagset size of 102.

import nltk

from nltk.corpus import brown

# pulls in the pre-tagged sents
brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]


ngram_tagger = nltk.NgramTagger(2, train_sents)

for i in range(1,7):
	ngram_tagger = nltk.NgramTagger(i, train_sents)
	print(ngram_tagger.evaluate(test_sents))

# Estimate the training data required for these taggers, assuming a vocabulary size of 105 and a tagset size of 102.

# Well the point of a tagger is to tag the vocabulary. So we need one instance of each token for a unigram. And then each ngram would need to see all the possible contexts to really be accurate. So does that mean it would be 105 to the power of n for an ngram? That seems…way wrong.