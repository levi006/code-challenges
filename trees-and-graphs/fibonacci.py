"""
Write a function int fib(int n) that returns Fn. 
For example, if n = 0, then fib() should return 0. If n = 1, then it should return 1. 
For n > 1, it should return Fn-1 + Fn-2

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

>>> fibonacci(9)
34

>>>
"""

# a fibonacci number is the sum starting at 1, 0 
def fib_recurse(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib_recurse(n-1) + fib_recurse(n-2)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"