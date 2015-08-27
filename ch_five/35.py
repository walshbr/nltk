# ★ Write a program to classify contexts involving the word 'must' according to the tag of the following word. Can this be used to discriminate between the epistemic and deontic uses of 'must'?

# deontic - be obliged to; should (expressing necessity).
# epistemic - expressing an opinion about something that is logically very likely

import nltk
from nltk.corpus import brown

tagged_words = brown.tagged_words()
cfd = nltk.ConditionalFreqDist(tagged_words)
tagged_sents = brown.tagged_sents()

bigram_tags = list(nltk.bigrams(tagged_words))

words_following_must = []
for bigram in bigram_tags:
    # returns a list of the form [['of', 'years'], ['IN', 'NNS']]
    zipped_tag = [list(t) for t in zip(*bigram)]
    if zipped_tag[0][0] == 'must' or zipped_tag[0][0] == 'Must':
        words_following_must.append((zipped_tag[0][1], zipped_tag[1][1]))

tags_following_must = set([tag for (__,tag) in words_following_must])

for bigram in bigram_tags:
    zipped_tag = [list(t) for t in zip(*bigram)]
    if zipped_tag[0][0] == 'must' or zipped_tag[0][0] == 'Must':
        print(zipped_tag[0][0] + " " + zipped_tag[0][1])
        if zipped_tag[1][1] in ['BE', 'BE-HL', 'NN', 'NNS', 'NP-HL']:
            print("Context is likely epistemic")
        elif zipped_tag[1][1] in ['HV', 'HV-TL', 'DO',  'RB', 'RB-HL', 'VB', 'VB-HL', 'VB-TL', 'VBZ']:
            print("Context is likely deontic")
        else:
            print("Context is unclear")


# set of tags for must is ({'MD': 994, 'MD-HL': 4, 'NN': 4, 'NIL': 1})

# The set of tags that follow must is: 
# unhelpful:
# ["''", '*', ',', '.', 'ABN', 'ABX', 'AT', 'CC', 'IN',  
# 'PPS', 'PPSS','PPLS', 'PPO',  'NIL',

# epistemic - 'BE', 'BE-HL', 'NN', 'NNS', 'NP-HL',

# deontic
# 'HV', 'HV-TL', 'DO',  'RB', 'RB-HL', 'VB', 'VB-HL', 'VB-TL', 'VBZ']
