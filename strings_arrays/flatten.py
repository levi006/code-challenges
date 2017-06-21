"""Utilities for flattening/combining lists of parents/children."""


def flatten(L):
	"""Transforms a list of (parent, children) tuples. 

	Given a list of (parent, children) tuples where 'parent' is a string and 'children'
	is a comma separated string, write a function to transform the list of (parent, children)
	tuples into a list of (parent, child) tuples.  

		>>> flatten([('a', '1,2,3')])
		[('a', '1'), ('a', '2'), ('a', '3')]

		>>> flatten([('a', '1,2,3'), ('b', '4,5,6')])
		[('a', '1'), ('a', '2'), ('a', '3'), ('b', '4'), ('b', '5'), ('b', '6')]

		>>> flatten([('Fyodor', 'Dmitri,Ivan,Alexei')])
		[('Fyodor', 'Dmitri'), ('Fyodor', 'Ivan'), ('Fyodor', 'Alexei')]
	"""

	flattened = []

	for parent, children in L:
		children_list = children.split(",") 

		for child in children_list:
			tup = (parent, child)
			flattened.append(tup)

	return flattened

def combine(L):
	"""Combines (parent, child) tuples into (parent, children) tuples.

		>>> combine([('Fyodor', 'Dmitri'), ('Fyodor', 'Ivan'), ('Fyodor', 'Alexei')])
		[('Fyodor', 'Dmitri,Ivan,Alexei')]

		>>> combine([('a', '1'), ('a', '2'), ('a', '3'), ('b', '4'), ('b', '5'), ('b', '6')])
		[('a', '1,2,3'), ('b', '4,5,6')]
	"""	

	pairs_dict = {}

	for parent, child in L:
		
		if parent not in pairs_dict:
			pairs_dict[parent] = child

		else:
			pairs_dict[parent] += "," + child

	return list(pairs_dict.items())

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n" 
