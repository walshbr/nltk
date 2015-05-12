# ◑ Study the lolcat version of the book of Genesis, accessible as nltk.corpus.genesis.words('lolcat.txt'), and the rules for converting text into lolspeak at http://www.lolcatbible.com/index.php?title=How_to_speak_lolcat. Define regular expressions to convert English words into corresponding lolspeak words.


import nltk
import re

from nltk.corpus import genesis

# now just need to write all the regex patterns you need to find the different examples they give.

conversions = [['ight', 'iet'], ['i', 'ai'], ['y\s', 'eh '], ['he\s', 'him '], ['his\s', 'him '], ['she\s', 'her'], ['\shers\s', ' her'], ['they', 'dem'], ['their', 'dem'], ['y\s', 'eh'], ['th','f'], ['Th', 'F'], ['I\s', 'Ai '], ['I\sam', 'Iz'], ['me', 'meh'], ['you', 'yu'], ['them', 'dem'], ['le\s', 'el '], ['le\s', 'el '], ['ee', 'ea'], ['oa', 'ow'], ['er\s', 'ah']]

text = 'When I talk to you, you make certain assumptions about me as a person based on what you’re hearing. You decide whether or not I might be worth paying attention to, and you develop a sense of our social relations based around the sound of my voice. The voice conveys and generates assumptions about the body and about power: am I making myself heard? Am I registering as a speaking voice? Am I worth listening to?'

for c in conversions:
	old_letters = c[0]
	pattern = re.compile(r'(' + old_letters + ')')
	new_letters = c[1]
	text = pattern.sub(new_letters, text)

print(text)