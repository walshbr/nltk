import nltk
from nltk.corpus import genesis
from nltk.corpus import gutenberg
from nltk import *
import pylab
import numpy as np 
import random
from nltk import tokenize
import random

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        new_word = random_word(text, 100)
        word = cfdist[new_word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
text_two = gutenberg.words('austen-emma.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

def random_word(words, n):
	random_cfd = FreqDist(words)
	choices = random_cfd.most_common(n)
	random_word= list(random.choice(choices))[0]
	return	random_word

thing_one = random_word(text, 100)
thing_two = random_word(text_two, 100)
generate_model(cfd, thing_one, 30)
print("")
generate_model(cfd, thing_two, 30)


# cfd['living']

#need help from Eric