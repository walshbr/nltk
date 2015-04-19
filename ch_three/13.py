# ☼ What is the difference between calling split on a string with 
# no argument or with ' ' as the argument, e.g. sent.split() versus
# sent.split(' ')? What happens when the 
# string being split contains tab characters, consecutive space characters, 
# or a sequence of tabs and
# spaces? (In IDLE you will need to use '\t' to enter a tab character.

no argument defaults to split on all white space characters.
a space as an argument means that it will split only on spaces and preserve the other stuff.