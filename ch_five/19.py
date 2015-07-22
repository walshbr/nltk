# 19. The evaluate() method works out how accurately the tagger performs on this text. For example, if the supplied
# tagged text was [('the', 'DT'), ('dog', 'NN')] and the tagger produced the output [('the', 'NN'), ('dog',
# 'NN')], then the score would be 0.5. 

#Let's try to figure out how the evaluation method works:
# 1. A tagger t takes a list of words as input, and produces a list of tagged words as output. However, t.evaluate()
# is given correctly tagged text as its only parameter. What must it do with this input before performing the
# tagging?

# it must run the correctly tagged text against its tagging model. and then it will calculate how similar its tagged version is to the correctly tagged model.

# 2. Once the tagger has created newly tagged text, how might the evaluate() method go about comparing it with
# the original tagged text and computing the accuracy score?

# The words themselves are largely irrelevant. It could just go through the second term of each tuple. Then it would count count how many identical terms they have.

# 3. Now examine the source code to see how the method is implemented. Inspect nltk.tag.api.__file__ to
# discover the location of the source code, and open this file using an editor (be sure to use the api.py file and not
# the compiled api.pyc binary file).