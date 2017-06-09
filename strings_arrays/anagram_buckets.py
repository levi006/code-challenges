def anagram_buckets(words):
	"""
	Given an array of words, print all anagrams together

	>>> anagram_buckets(['cat', 'atc', 'banana', 'cool', 'loco'])
	[['banana'], ['cool', 'loco'], ['cat', 'atc']]


	"""

	word_dict = {}

	for word in words:
		sorted_word = "".join(sorted(word))
		
		if sorted_word in word_dict:
			word_dict[sorted_word].append(word)

		else:
			word_dict[sorted_word] = [word]

	print word_dict

	res = []

	for sorted_word, word in word_dict.iteritems():
			res.append(word)
	return res



if __name__ == "__main__":
	import doctest
	doctest.testmod()