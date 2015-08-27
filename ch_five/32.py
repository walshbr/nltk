# ◑ Consult the documentation for the Brill tagger demo function, using help(nltk.tag.brill.demo). Experiment with the tagger by setting different values for the parameters. Is there any trade-off between training time (corpus size) and performance?

import nltk
from nltk.corpus import brown

from nltk.tag.brill import *
from nltk.tag import brill_trainer

templates = nltk.tag.brill.nltkdemo18()
trainer = nltk.brill_trainer.BrillTaggerTrainer(initial_tagger=nltk.DefaultTagger('NN'),
templates=templates, trace=3,
deterministic=True)

brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.5)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

tagger = trainer.train(train_sents, max_rules=20, min_score=2, min_acc=None)
print(tagger.evaluate(test_sents))