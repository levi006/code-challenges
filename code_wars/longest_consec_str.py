"""
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.


>>> longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)
'abigailtheta'

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

"""

def longest_consec(strarr,k):
    string_dict = {}

    # .get() returns value for key
    
    # key = len(strarr[0])
    # value = strarr[0]
    # string_dict[key] = value

    #create dictionary {'word': word_len}
    for i in range(len(strarr)):
        string_dict[strarr[i]] = len(strarr[i])
    # print "dictionary is " + str((string_dict))
    # print "list of items in string_dict: " + str(string_dict.items())
    print string_dict

    longest_len = max(string_dict.values())
    print "longest length is: " + str(longest_len)

    word_count = sorted(string_dict.values())
    print "sorted list of word counts: " + str(word_count)
    print "sorted list by alphabetized keys: " + str(sorted(string_dict.items()))
    print "sorted list of alphabetized keys: " + str(sorted(string_dict.keys()))
    max_value = max(map(int, string_dict.values()))
    print "max_length: " + str(max_value)


    for word, length in string_dict.iteritems():
        if max_value == length:
            print word
            print list(string_dict.keys())[list(string_dict.values()).index(length)] # Prints george

   



    # for i in range(k):
 
    
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"],2)
