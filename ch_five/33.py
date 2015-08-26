# ◑ Write code that builds a dictionary of dictionaries of sets. Use it to store the set of POS tags that can follow a given word having a given POS tag, i.e. wordi → tagi → tagi+1.

import nltk
from nltk.corpus import brown

tags = brown.tagged_words(categories='news')[0:3000]
bigram_tags = list(nltk.bigrams(tags))
tags = set(tags)

def find_tag_context(given_word, given_tag):
    # for the given tag, goes through and searchs for all instances of that tag. returns all the parts of speech that immediately follow it.
    bigram_contexts = []
    for bigram in bigram_tags:
        if (given_word, given_tag) == bigram[0]:
            bigram_contexts.append(bigram[1][1])
    return bigram_contexts

all_contexts = {}

for (word, word_tag) in tags:
    new_contexts = set(find_tag_context(word, word_tag))
    if new_contexts:
        all_contexts[(word, word_tag)] = new_contexts
    else:
        all_contexts[(word, word_tag)] = "No contexts of this type"
    # all_contexts.append(((word, word_tag), set(find_tag_context(word, word_tag))))

print(all_contexts)