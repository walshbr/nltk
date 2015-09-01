# ★ Our approach for tagging an unknown word has been to consider the letters of the word (using RegexpTagger()), or to ignore the word altogether and tag it as a noun (using nltk.DefaultTagger()). These methods will not do well for texts having new words that are not nouns. Consider the sentence 'I like to blog on Kim's blog'. If blog is a new word, then looking at the previous tag (TO versus NP$) would probably be helpful. I.e. we need a default tagger that is sensitive to the preceding tag.
# Create a new kind of unigram tagger that looks at the tag of the previous word, and ignores the current word. (The best way to do this is to modify the source code for UnigramTagger(), which presumes knowledge of object-oriented programming in Python.)
# Add this tagger to the sequence of backoff taggers (including ordinary trigram and bigram taggers that look at words), right before the usual default tagger.
# Evaluate the contribution of this new unigram tagger.

import nltk
from nltk.corpus import brown
from nltk.tag.sequential import UnigramTagger
from nltk import jsontags
import pprint


tagged_sents = brown.tagged_sents(categories='news')

size = int(len(tagged_sents) * 0.9)
train_sents = tagged_sents[:size]
test_sents = tagged_sents[size:]


@jsontags.register_tag
class PreviousTagger(UnigramTagger):
    json_tag = 'nltk.tag.sequential.PreviousTagger'

    def context(self, tokens, index, history):
        if index == 0:
            return None
        else:
            return history[index-1]


t0 = nltk.DefaultTagger('NN')
t1 = PreviousTagger(train_sents, backoff=t0)
t2 = nltk.UnigramTagger(train_sents, backoff=t1)
t3 = nltk.BigramTagger(train_sents, backoff=t2)
t4 = nltk.TrigramTagger(train_sents, backoff=t3)

pprint.pprint(t4.tag(['I', 'like', 'to', 'blog', 'on', 'Kim\'s', 'blog']))
