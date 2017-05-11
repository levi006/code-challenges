
def diff_lists(list_one,list_two):
	"""
	diff_lists() returns the difference between two iterables, while retaining the order of the original lists.

	>>> diff_lists(["apple", "berry", "cherry","durian"], ["apple", "cherry", "eiderdown", "yams"])
	>>> ["berry", "durian"] ["eiderdown", "yams"]

	You can also do this with sets, but you would lose the order of the lists (if this is important). If the order is important, sets would be an O(n) to achieve this. 

	ex. 

	def diff_lists(list_one, list_two):
		diff_one = list(set(list_one) - set(list_two))
		diff_two = list(set(list_two) - set(list_one))
	
		return diff_one, diff_two 

	Run time is O(n). However, in toy problems, it might be faster to look through a list than to construct a set.

	ex. 

	def diff_lists(list_one, list_two):
		diff_one = []
		diff_two = []	
		
		for x in list_one:
			if x in list_one and x not in list_two:
				diff_one.append(x)

		for x in list_two:
			if x in list_two and x not in list_one:
				diff_two.append(x)
		
		return diff_one, diff_two  

	Runtime is O(n^2) because of the for-loops, but this doesn't matter in toy situations. It would be slower to scale. But we would lose duplicates and the order of the original lists. 


	"""
	diff_one = []
	diff_two = []

	two_set = set(list_two)
	
	for item in list_one:
		if item not in two_set:
			diff_one.append(item)

	one_set = set(list_one)

	for item in list_two:
		if item not in one_set:
			diff_two.append(item) 
		
	return (diff_one, diff_two)
