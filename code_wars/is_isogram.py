"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

>>> is_isogram("Dermatoglyphics")
True

>>> is_isogram("aba")
False

It should ignore letter cases:

>>> is_isogram("moOse") 
False

"""

def is_isogram(string):
    lower_string = string.lower()
    seen = []
    
    for i in range(len(lower_string)):
        if lower_string[i] not in seen:
            seen.append(lower_string[i])
        elif lower_string[i] in seen:
            return False
    return True


if __name__ == "__main__":

	import doctest
	if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"