def anagram_buckets_v2(words):
	"""
	Given an array of words, print all anagrams together.

	>>> anagram_buckets_v2(['cat', 'atc', 'banana', 'cool', 'loco'])
	[['banana'], ['cool', 'loco'], ['cat', 'atc']]

	>>> anagram_buckets_v2(['python', 'thopny', 'ythonp'])
	[['python', 'thopny', 'ythonp']]

	"""

	word_dict = {"".join(sorted(word)): [] for word in words}
	
	for word in words:
		word_dict["".join(sorted(word))].append(word)

	print word_dict.values()



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n" 