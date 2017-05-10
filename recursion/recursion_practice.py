# given a list give a count of how many odd numbers are in it
"""
>>> odd_nums([12,3,45,7,2])
3
"""

# the count of odd in a list is 1 or 0 plus the count of odd numbers of a smaller list

def odd_nums(num_list):
	if num_list == []:
		return 0
	else:
		first = num_list[0]
		rest = num_list[1:]

		if first % 2 == 0:
			return 0 + odd_nums(rest)
					
		else:
			return 1 + odd_nums(rest)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"

