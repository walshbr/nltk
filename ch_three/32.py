# ◑ Define a variable silly to contain the string: 'newly formed bland ideas are inexpressible in an infuriating way'. (This happens to be the legitimate interpretation that bilingual English-Spanish speakers can assign to Chomsky's famous nonsense phrase, colorless green ideas sleep furiously according to Wikipedia). Now write code to perform the following tasks:

# Split silly into a list of strings, one per word, using Python's split() operation, and save this to a variable called bland.
# Extract the second letter of each word in silly and join them into a string, to get 'eoldrnnnna'.
# Combine the words in bland back into a single string, using join(). Make sure the words in the resulting string are separated with whitespace.
# Print the words of silly in alphabetical order, one per line.

silly = 'newly formed bland ideas are inexpressible in an infuriating way'

bland = silly.split(' ')

silly_word = ''

for word in bland:
	silly_word += word[1]
print(silly_word)

new_bland = ' '.join(bland)
print(new_bland)
print(bland)

bland = sorted(bland)
for w in bland:
	print(w)