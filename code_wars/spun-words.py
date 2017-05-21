"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


>>> spin_words("Hey fellow warriors")
'Hey wollef sroirraw'

"""


def spin_words(sentence):
    def spin(word):
        if len(word) >= 5:
            return reduce(lambda x,y: x + y, reversed(word), "")
        else:
            return word
    return ' '.join(map(spin, sentence.split()))

if __name__ == "__main__":

	import doctest
	if doctest.testmod().failed == 0:
		print "\n*** ALL TESTS PASSED. GO YOU!\n"

    