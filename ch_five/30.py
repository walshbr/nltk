# ◑ Preprocess the Brown News data by replacing low frequency words with UNK, but leaving the tags untouched. Now train and evaluate a bigram tagger on this data. How much does this help? What is the contribution of the unigram tagger and default tagger now?

"""def helps a lot when working with a solo bigram tagger. doesn't help so much when there are backoff taggers appropriately assigned. actually makes things worse in those cases. In those cases, the unigram and default taggers are just working on the words that wouldn't be part of bigrams at all? If a bigram works by tagging n and n-1 words, then the first word in a sentence won't have any context. So it will need a default/lookup tagger for it to work."""

import nltk
from nltk.corpus import brown
import modify

# getting the data ready

brown_tagged_sents = brown.tagged_sents(categories='news')

# finds the most common 100

fd = nltk.FreqDist(brown.words())
most_common = [tag for (tag,__) in fd.most_common(100)]

def unk(word, tag):
    if word in most_common:
        return word
    else:
        return 'UNK'

brown_tagged_sents = modify.modify_words(brown_tagged_sents, unk)

size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)

print(t2.evaluate(test_sents))
# baseline performance is 85% with all three taggers and unprocessed.
# baseline bigram tagger is 15%
# all three processed is 60%
