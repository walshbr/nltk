# ★ Rewrite the following nested loop as a nested list comprehension: 	
# >>> words = ['attribution', 'confabulation', 'elocution',
# ...          'sequoia', 'tenacious', 'unidirectional']
# >>> vsequences = set()
# >>> for word in words:
# ...     vowels = []
# ...     for char in word:
# ...         if char in 'aeiou':
# ...             vowels.append(char)
# ...     vsequences.add(''.join(vowels))
# >>> sorted(vsequences)
# ['aiuio', 'eaiou', 'eouio', 'euoia', 'oauaio', 'uiieioa']

words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']

vsequences = set()
vowels = []

# ask eric = you can't quite figure out how to include both into a single comprehension. Is it possible to have multiple expressions in each comprehension? The below seems to be the best I can do, but it's combining them all into a single item, since the vowels list isn't being reset each time.

vsequences = set([''.join([char for char in word if char in 'aeiou']) for word in words])

print(vsequences)