# ◑ Define the variable saying to contain the list ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']. Process this list using a for loop, and store the length of each word in a new list lengths. Hint: begin by assigning the empty list to lengths, using lengths = []. Then each time through the loop, use append() to add another length value to the list. Now do the same thing using a list comprehension.

saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']

lengths = []
for w in saying:
	lengths.append(len(w))
print(lengths)

# list comprehension version
lengths = [len(w) for w in saying]
print(lengths)
