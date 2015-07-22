# ◑ Use sorted() and set() to get a sorted list of tags used in the Brown corpus, removing duplicates.

from nltk.corpus import Brown

tags = brown.tagged_words()
sorted_tags = sorted(tags)
unique_tags = set(sorted_tags)
vals =[val for key, val in unique_tags]	
print(sorted(set(vals)))