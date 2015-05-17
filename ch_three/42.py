# ★ Use WordNet to create a semantic index for a text collection. Extend the concordance search program in 3.6, indexing each word using the offset of its first synset, e.g. wn.synsets('dog')[0].offset (and optionally the offset of some of its ancestors in the hypernym hierarchy).

import nltk.corpus

from nltk.corpus import wordnet as wn
from nltk.corpus import genesis

class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))
        

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/4)                # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
            print(ldisplay, rdisplay)

    def _stem(self, word):
        return self._stemmer.stem(word).lower()

porter = nltk.PorterStemmer()
grail = nltk.corpus.webtext.words('grail.txt')

text = genesis.words()

def sem_index(text):

    word_with_syns = []
    # iterate over every word in the text
    for word in text:
        # synsets are equal to all the synsets for the word
        synsets = wn.synsets(word)
        syns_indices = []
        # for every synset in the synset grouping
        for synset in synsets:
            #set the index number equal to its offset
            sem_index_num = synset.offset()
            syns_indices += [sem_index_num]    
        if syns_indices:
            word_with_syns.extend((word, syns_indices))
        else:
            word_with_syns.extend((word, 'no synonyms'))
    return word_with_syns

sem_index_nums = sem_index(text)
print(sem_index_nums[0:100])
# text_with_index = [], [(sem_index, word) for tup in sem_index_nums]