def modify_tags(corpus, f):
    """Modify the tags in a corpus with f."""
    new_corpus = []
    for sent in corpus:
        new_corpus.append([(w, f(w, t)) for (w, t) in sent])
    return new_corpus

def modify_words(corpus, f):
	"""Modify the words in a corpus with f but leave the tags untouched"""
	new_corpus = []
	for sent in corpus:
		new_corpus.append([(f(w, t), t) for (w, t) in sent])
	return new_corpus