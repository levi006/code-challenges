#two words are anagrams if they have the same frequency of characters 

def find_anagrams(words, word):  
    """
    Given 
- A dictionary file
- An input word

Find all words in the dictionary that are anagrams of the input word.

Ex:
Dictionary:
- CAT
- FACT
- TAC
- ACT
- AT

Word:
- ACT

Output:
- ACT
- CAT
- TAC

 >>> find_anagrams(['cat', 'fact', 'tac', 'act', 'at'], 'act')
 ['act', 'cat', 'tac']
 
    """
    results = []
    sorted_word = "".join(sorted(word))

    for w in words:
        sorted_w = "".join(sorted(w))   
        if sorted_w == sorted_word:
            # print w, sorted_word
            results.append(w)
    return sorted(results) 


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"          