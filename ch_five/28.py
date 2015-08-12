# ◑ Experiment with taggers using the simplified tagset (or make one of your own by discarding all but the first character of each tag name). Such a tagger has fewer distinctions to make, but much less information on which to base its work. Discuss your findings.

import nltk
from nltk.corpus import brown

# getting the data ready

brown_tagged_sents = brown.tagged_sents(categories='news')
simplified_tagged_sents = []

# strips out all but the first letter for the tagsets and dumps them in a new array.

for sent in brown_tagged_sents:
    sent_to_append = []
    for (word, tag) in sent:
        sent_to_append.append((word, tag[0]))
    simplified_tagged_sents.append(sent_to_append)

size = int(len(simplified_tagged_sents) * 0.9)
train_sents = simplified_tagged_sents[:size]
test_sents = simplified_tagged_sents[size:]


t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
