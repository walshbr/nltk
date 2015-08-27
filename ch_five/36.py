# ★ Create a regular expression tagger and various unigram and n-gram taggers, incorporating backoff, and train them on part of the Brown corpus.
# Create three different combinations of the taggers. Test the accuracy of each combined tagger. Which combination works best?

# the best combination is the kind that moves from most specific to most general. So the default tagger and the regex tagger are the last backoff.

# Try varying the size of the training corpus. How does it affect your results?

import nltk
from nltk.corpus import brown

# getting the data ready

tagged_sents = brown.tagged_sents(categories='news')

size = int(len(tagged_sents) * 0.99)
train_sents = tagged_sents[:size]
test_sents = tagged_sents[size:]


patterns = [
     (r'.*ing$', 'VBG'),               # gerunds
     (r'.*ed$', 'VBD'),                # simple past
     (r'.*es$', 'VBZ'),                # 3rd singular present
     (r'.*ould$', 'MD'),               # modals
     (r'.*\'s$', 'NN$'),               # possessive nouns
     (r'.*s$', 'NNS'),                 # plural nouns
     (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
     (r'.*', 'NN')                     # nouns (default)
     ]


t0 = nltk.DefaultTagger('NN')
tr = nltk.RegexpTagger(patterns, backoff=t0)
t1 = nltk.UnigramTagger(train_sents, backoff=tr)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
print(t2.evaluate(test_sents))
