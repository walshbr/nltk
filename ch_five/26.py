# ◑ 4.1 plotted a curve showing change in the performance of a lookup tagger as the model size was increased. Plot the performance curve for a unigram tagger, as the amount of training data is varied.

import nltk
from nltk.corpus import brown
import pylab
 	
def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return nltk.tag.accuracy(baseline_tagger, nltk.corpus.brown.tagged_sents(categories='news'))

def display():

    words_by_freq = nltk.FreqDist(nltk.corpus.brown.words(categories='news')).sorted()
    cfd = nltk.ConditionalFreqDist(nltk.corpus.brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.semilogx(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

display()