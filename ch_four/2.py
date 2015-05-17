# 2. ☼ Identify three operations that can be performed on both tuples and lists. Identify three list operations that cannot be performed on tuples. 
both tuples and lists

__add__
__contains__
__eq__

lists but not tuples

__delitem__ for lists (because a tuple isn't organized in such a way as to allow that?)
__iadd__ for lists
also reverse() and sort(). because a tuple isn't indexed/stored in that same way.

# Name a context where using a list instead of a tuple generates a Python error.

###### question here - 

# storing data of different types in a list would cause an error. lists are meant to store data of similar structure and types.

# also storing stuff as a tuple that is meant to be mutable would cause errors - because tuples are immutable and can't be changed. but thsose both seem like errors in the sense that they would produce problems, not in the sense that it would break python outright. are there other more flagrant misuses that i'm missing?
