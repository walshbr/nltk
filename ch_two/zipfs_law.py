import nltk
from nltk.corpus import gutenberg
from nltk import *
import pylab
import numpy as np 
import random
from nltk import tokenize


random_string = ""

for x in range(0, 1000000):
	random_string = random_string + random.choice("abcdefg ")

text = gutenberg.words(fileids='austen-emma.txt')
freq = FreqDist(text)

top_150 = freq.most_common(150)[0:149]

x = np.array(pylab.arange(0, 149, 1))
y = []
for word, freq in top_150:
	y.append(freq)
y = np.array(y)

pylab.xlabel('Rank (Index Position)')
pylab.ylabel('Word Frequencies')
pylab.plot(x, y)
pylab.show()
new_words = nltk.word_tokenize(random_string)
random_freq = FreqDist(text)
random_top_150 = random_freq.most_common(150)[0:149]
y = []
for word, freq in random_top_150:
	y.append(freq)
y = np.array(y)

# print(random_top_150)

pylab.plot(x, y)
pylab.show()

# 23 part 2 - you just need to tokenize and then plot the graph
