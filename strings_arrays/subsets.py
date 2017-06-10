def get_subsets(s):
	"""
	Given a list of elements, return a list of all possible subsets.

	>>> get_subsets(['a', 'b', 'c'])
	[['a', 'b', 'c'], ['b', 'c'], ['a', 'c'], ['c'], ['a', 'b'], ['b'], ['a'], []]
	
	"""

	if len(s) < 1:
		return [[]]

	subsets = get_subsets(s[1:])
	results = []

	for subset in subsets:
		results.append([s[0]] + subset)
		results.append(subset)

	return results

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n" 