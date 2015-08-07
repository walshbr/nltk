# ◑ Inspect the confusion matrix for the bigram tagger t2 defined in 5, and identify one or more sets of tags to collapse. Define a dictionary to do the mapping, and evaluate the tagger on the simplified data.

import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)

# produces all the tags for the test data

test_tags = [tag for sent in brown.sents(categories='editorial') for (word, tag) in t2.tag(sent)]

# produces all the golden tags

gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]

print(nltk.ConfusionMatrix(gold_tags, test_tags)) 