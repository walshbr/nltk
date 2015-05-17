# 3. ☼ Find out how to create a tuple consisting of a single item. There are at least two ways to do this.


Would this be what they have in mind? declaring it and converting it from a list?

thing_two = ('word',)

thing_three = ['word']
tuple(thing_three)

Can't convert from a string because it will iterate over the string and give a separate object for each character.