# ☼ Learn about the affix tagger (type help(nltk.AffixTagger)). Train an affix tagger and run it on some new text. Experiment with different settings for the affix length and the minimum word length. Discuss your findings.


import nltk
from nltk.corpus import brown
from nltk.corpus import gutenberg

text = gutenberg.words('austen-persuasion.txt')

brown_sents = brown.sents(categories='news')
brown_tagged_sents = brown.tagged_sents(categories='news')
affix_tagger = nltk.AffixTagger(train=brown_tagged_sents, affix_length=1, min_stem_length=3)
print(affix_tagger.tag(text))