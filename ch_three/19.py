# Create a file consisting of words and (made up) frequencies, where each line consists of a word, the space character, and a positive integer,
# e.g. fuzzy 53. Read the file into a Python list using open(filename).readlines(). Next, break each line into its two fields using split(),
# and convert the number into an integer using int(). The result should be a list of the form: [['fuzzy', 53], ...].

# reads in a text line by line and strips out new lines
f = open('freq.txt')
f = [line.strip() for line in f]

# splits the lines into their component pieces
result = [line.split(' ') for line in f]

# converts the numbers to integers

for item in result:
	item[1] = int(item[1]) 

# prints out a test case to prove that the numbers are numbers
# and not strings
print(result[0][1]*10)