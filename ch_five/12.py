# ☼ Train a bigram tagger with no backoff tagger, and run it on some of the training data. Next, run it on some new data. What happens to the performance of the tagger? Why?

from nltk.corpus import gutenberg
from nltk.corpus import brown
import nltk

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
size = int(len(brown_tagged_sents) * 0.7)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

bigram_tagger = nltk.BigramTagger(train_sents)
bigram_tagger.evaluate(train_sents)
bigram_tagger.evaluate(test_sents)

# the performance drops off considerably because it relies on the stastical probablity that word is a particular part of speech based on the first word in a bigram. So when it gets to a new word that it hasn't seen in a bigram before it has nothing to go on and the word is returned as unknown. The accuracy plummets.