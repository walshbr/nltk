import nltk
import nltk.corpus
from nltk.corpus import wordnet as wn

# print(wn.synsets('car'))

pairs = ['car', 'automobile'], ['gem', 'jewel'], ['journey', 'voyage'], ['boy', 'lad'], ['coast', 'shore'], ['asylum', 'madhouse'], ['magician', 'wizard'], ['midday', 'noon'], ['furnace', 'stove'], ['food', 'fruit'], ['bird', 'cock'], ['bird', 'crane'], ['tool', 'implement'], ['brother', 'monk'], ['lad', 'brother'], ['crane', 'implement'], ['journey', 'car'], ['monk', 'oracle'], ['cemetery', 'woodland'], ['food', 'rooster'], ['coast', 'hill'], ['forest', 'graveyard'], ['shore', 'woodland'], ['monk', 'slave'], ['coast', 'forest'], ['lad', 'wizard'], ['chord', 'smile'], ['glass', 'magician'], ['rooster', 'voyage'], ['noon', 'string']
first_synsets = []
second_synsets = []

counter = 0
number_of_paths = 0
average_similarity = 0
total_similarity = 0
pairs_with_averages = []
print(pairs)
for first, second in pairs:
	first_synsets = wn.synsets(first)
	second_synsets = wn.synsets(second)
	print(pairs[counter])
	for first_synset in first_synsets:
		for second_synset in second_synsets:
			similarity = first_synset.path_similarity(second_synset)
			total_similarity += similarity
			number_of_paths += 1
	average_similarity = total_similarity / number_of_paths
	print('total similarity: ', total_similarity)
	print('number of paths: ', number_of_paths)
	print('average similarity: ', average_similarity)
	print('\n')
	total_similarity = 0
	number_of_paths = 0
	average_similarity = 0
	counter += 1


