"""
>>> two_sum([1, 6, -5, 7, 3], -2)
[2, 4]

>>> two_sum([1, 9, 10], 8)
[-1, -1]
"""
def two_sum(nums, target):
	check = {}

	for i,num in enumerate(nums):
	    if num not in check:
	        check[target - num]=i
	    else:
	        return [min(i,check[num]),max(i,check[num])]
	return [-1,-1]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"

