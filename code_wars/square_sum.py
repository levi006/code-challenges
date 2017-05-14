"""Complete the squareSum method so that it squares each number passed into it and then sums the results together.

>>> square_sum([1, 2, 2]) 
9

>>> square_sum([0, 3, 4, 5]) 
50

"""

def square_sum(numbers):
	sum = 0
	for num in numbers:
		sum = sum + num*num
	return sum

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"