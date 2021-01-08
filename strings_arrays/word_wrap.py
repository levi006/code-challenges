"""
>>> wrap("foo bar baz", 4)
"foo\nbar\nbaz"

>>> wrap("foo bar baz", 9)
"foo bar\nbaz"
"""
#tracking current max white space indice while indice < l



# if len word > l:
    #raise exception("word should never be longer than l") 

# s, l
# words delimited by a space 
    
    
# if len of word < l,
# split by " " delimiter [foo, bar, baz]
# append "\n" to each word, concatenate each word

def wrap(s,l):

    words = s.split(" ")

    # while line is less than max length, continue adding words
    line = ""

    for word in words: #[foo, bar, baz]
        if len(line) > l:
             = word

        # else, wrap with \n        
        else:
            line = line + "\n"
            
# track lines in lines array, join at end

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"

