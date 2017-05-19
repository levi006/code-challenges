"""
PROBLEM 6: Python

Notes: The given link "http://www.infomat.net/infomat/library/aliceinwonderland.txt" was a dead link, so I substituted The Gutenberg Projects version of Alice in Wonderland. I provided both a link and a static option in the script in case the user had no internet access. 
"""

import urllib, re
from collections import Counter

def word_frequencies():

	link = 'http://www.gutenberg.org/files/11/11-0.txt'
	f = urllib.urlopen(link)

	# static link in case there's no internet connection
	# f = open("alice.txt")

	words = re.findall('\w+', f.read().lower())

	for x in (Counter(words).most_common(15)):
		print str(x[0]) + " | " + str(x[1])
	return

word_frequencies()