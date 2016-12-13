"""
Figure out if a given number is prime. 

>>> is_prime(0)
False

>>> is_prime(1)
False

>>> is_prime(2)
True

>>> is_prime(3)
True

>>> is_prime(4)
False

"""

def is_prime(num):

	if num < 2:
		return False

	for i in range(2, num):
		if num % i == 0:
			return False
	return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU MET YOUR PRIME DIRECTIVE!\n"