# What is the upper limit of performance for a lookup tagger, assuming no limit to the size of its table? (Hint: write a
# program to work out what percentage of tokens of a word are assigned the most likely tag for that word, on average.)

# use the training data to figure out how often 


import nltk
from nltk.corpus import brown


fd = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))

avgs = []
for (word, freqs) in cfd.items():
    n = float(freqs.N())
    max_tag = freqs.max()
    avg = freqs[max_tag] / n
    print('likelihood for {} = {}'.format(word, avg))
    avgs.append(avg)

print('')
print('average correct = {}'.format(sum(avgs) / len(avgs)))