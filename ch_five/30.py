# ◑ Preprocess the Brown News data by replacing low frequency words with UNK, but leaving the tags untouched. Now train and evaluate a bigram tagger on this data. How much does this help? What is the contribution of the unigram tagger and default tagger now?

import nltk
from nltk.corpus import brown

# getting the data ready

brown_tagged_sents = brown.tagged_sents(categories='news')

fd = nltk.FreqDist(brown.words())
most_common_100 = [tag for (tag,__) in fd.most_common(100)]

for sent in brown_tagged_sents:
    for (word, tag) in sent:
        if word not in most_common_100:
            word = word.replace(word, 'UNK')

    #     sent_to_append.append((word, tag[0]))
    # simplified_tagged_sents.append(sent)

size = int(len(simplified_tagged_sents) * 0.9)
train_sents = simplified_tagged_sents[:size]
test_sents = simplified_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)