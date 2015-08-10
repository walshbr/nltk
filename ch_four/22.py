# ◑ Import the itemgetter() function from the operator module in Python's standard library (i.e. from operator import itemgetter). Create a list words containing several words. Now try calling: sorted(words, key=itemgetter(1)), and sorted(words, key=itemgetter(-1)). Explain what itemgetter() is doing.

from operator import itemgetter

words = ['this', 'is', 'my', 'list', 'of', 'words']