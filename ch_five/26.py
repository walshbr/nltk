# ◑ 4.1 plotted a curve showing change in the performance of a lookup tagger as the model size was increased. Plot the performance curve for a unigram tagger, as the amount of training data is varied.

import nltk
from nltk.corpus import brown
from random import shuffle

def performance(cfd, wordlist):
    # takes in a conditional frequency and a wordlist

    # goes through every word iun the wordlist and returns a dictionary consisting of the word and the most frequent tag for that word.
    lt = dict((word, cfd[word].max()) for word in wordlist)

    # the baseline tagger is fed the resultant list of tagged words as a model. and given the default tagger to make everything else a noun.

    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))

    # returns the evaluation score for the tagger
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    import pylab

    # pulls in a frequency distribution of all the words in the news category
    word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
    # sequentially orders the words by frequency
    words_by_freq = [w for (w, _) in word_freqs]
    # makes a cfd based on the words and the frequency of their tags
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))

    # returns a list of evenly spaced numbers from 1 to two to the power of fifteen
    sizes = 2 ** pylab.arange(15)

    # for every size in that evenly spaced array, evaluate a baseline tagger based on a training set of that size. so it's plotting training models that get larger and larger.
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')

    # sets all of the axes
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

display()