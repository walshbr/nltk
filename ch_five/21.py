# ◑ In 3.1 we saw a table involving frequency counts for the verbs adore, love, like, prefer and preceding qualifiers absolutely and definitely. Investigate the full range of adverbs that appear before these four verbs.

from nltk.corpus import brown
import nltk

tagged_text = brown.tagged_words(tagset='universal')
tagged_bigrams = list(nltk.bigrams(tagged_text))

for bigram in tagged_bigrams:
	zipped_tag = [list(t) for t in zip(*bigram)]
	if zipped_tag[0][1] in ['adore', 'love', 'prefer', 'like'] and zipped_tag[1][1] == 'VERB' and zipped_tag[1][0] == 'ADV':
		print(zipped_tag[0][0])
