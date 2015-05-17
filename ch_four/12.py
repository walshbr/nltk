# 12. Initialize an n-by-m list of lists of empty strings using list multiplication, e.g. word_table = [[''] * n] * m.
# What happens when you set one of its values, e.g. word_table[1][2] = "hello"? Explain why this happens. Now
# write an expression using range() to construct a list of lists, and show that it does not have this problem.

n = 3
m = 3

word_table = [[''] * n] * m

print(word_table)
word_table[1][2] = 'hello'
print(word_table)

# it has this problem because you're changing one of the underlying lists which is being referenced.

new_word_table = []
new_word_table[range(3)] = []

print(new_word_table)