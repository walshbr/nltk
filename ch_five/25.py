# ◑ Obtain some tagged data for another language, and train and evaluate a variety of taggers on it. If the language is morphologically complex, or if there are any orthographic clues (e.g. capitalization) to word classes, consider developing a regular expression tagger for it (ordered after the unigram tagger, and before the default tagger). How does the accuracy of your tagger(s) compare with the same taggers run on English data? Discuss any issues you encounter in applying these methods to the language.

import nltk
from nltk.corpus import floresta

text = floresta.words()
floresta_tagged_sents = floresta.tagged_sents()
floresta_tagged_words = floresta.tagged_words()
fd = nltk.FreqDist(text)
cfd = nltk.ConditionalFreqDist(floresta_tagged_words)
most_freq_words = fd.most_common(100)

# lookup tagger for likely tags
likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model=likely_tags)


# trained unigram tagger
size = int(len(floresta_tagged_sents) * 0.9)
training_data = tagged_text[:size]
test_data = tagged_text[size:]

uni_tagger = nltk.UnigramTagger(model=training_data)
uni_tagger.evaluate(test_data)