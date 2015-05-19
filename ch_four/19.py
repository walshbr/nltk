# ◑ Write a list comprehension that sorts a list of WordNet synsets for proximity to a given synset. For example, given the synsets minke_whale.n.01, orca.n.01, novel.n.01, and tortoise.n.01, sort them according to their shortest_path_distance() from right_whale.n.01.

from nltk.corpus import wordnet

synsets = ['minke_whale.n.01', 'orca.n.01', 'novel.n.01', 'tortoise.n.01']

synset_to_check = 'right_whale.n.01'


#####
# i'm trying to sort based on this list comprehension:

[(wordnet.path_similarity(wordnet.synset('right_whale.n.01'), wordnet.synset(synset)), synset) for synset in synsets]

just need to wrap that outer layer in sorted() like so:

[sorted((wordnet.path_similarity(wordnet.synset('right_whale.n.01'), wordnet.synset(synset)), synset), key=lambda x: x[0]) for synset in synsets]

but the lambda thing isn't quite working:

# >>> [sorted((wordnet.path_similarity(wordnet.synset('right_whale.n.01'), wordnet.synset(synset)), synset), key=lambda x: x[0]) for synset in synsets]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
#   File "<stdin>", line 1, in <lambda>
# TypeError: 'float' object is not subscriptable

seems to be trying to subscript the first term? is it going through and trying to sort each term in the tuple? or is something else going on?