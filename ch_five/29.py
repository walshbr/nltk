# ◑ Recall the example of a bigram tagger which encountered a word it hadn't seen during training, and tagged the rest of the sentence as None. It is possible for a bigram tagger to fail part way through a sentence even if it contains no unseen words (even if the sentence was used during training). In what circumstance can this happen? Can you write a program to find some examples of this?

"""So the idea is that once a bigram tagger doesn't recognize a word, it will suddenly have chain reaction where everything becomes unknown. Because it doesn't know how to account for pairs of tags that have unknowns in them, each subsequent tag pair will have an unknown. AND CHAOS WILL WASH OVER THE EARTH.

So the answer here is yes it is possible - because even if it has seen all the words before it could see them in different contexts. 

A program to find examples of this would pull out all the extant bigrams containing a particular word in the training set. And then it would do the same for the testing set. Subtract the training set from the testing set. If anything remains, it is a bigram context that is not accounted for.

"""


import nltk
from nltk.corpus import brown
from random import shuffle

brown_tagged_sents = brown.tagged_sents(categories='news')

training_set = brown_tagged_sents[0]
training_sentence = brown.sents()[0]

shuffled_sentence = sorted(training_sentence)

bigram_training = list(nltk.bigrams(shuffled_sentence))
bigram_shuffled = list(nltk.bigrams(training_sentence))

def test_unknown_contexts(corpus_one, corpus_two):
    """tests to see if two inputted sentences are identical"""
    if list(set(corpus_one)-set(corpus_two)):
        print("There are unknown contexts")
    else:
        print("All contexts are known")

test_unknown_contexts(bigram_training, bigram_shuffled)

