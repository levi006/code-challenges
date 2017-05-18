"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

>>> sort_array([5, 3, 2, 8, 1, 4])
[1, 3, 2, 8, 5, 4]

>>> sort_array([3,3,3])
"""

def sort_array(source_array):
    if source_array == []:
        return []
    
    odds = []    
    for num in source_array:
        if num % 2 == 1:
        	print("num: ", num)
        	
        	odds.append(source_array.pop(source_array.index(num)))
    


    # for num in source_array:
	   #  if num%2 == 1:
    #     	print source_array[num]
    #     	# odds[source_array[num]]

    # return source_array



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.\n"