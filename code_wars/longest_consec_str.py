"""
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.


>>> longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)
'abigailtheta'

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

"""

# def longest_consec(strarr,k):
#     string_dict = {}

#     # create dictionary {'word': word_len}
#     for i in range(len(strarr)):
#         string_dict[strarr[i]] = len(strarr[i])

#     longest_str = ''    

#     longest_len = max(string_dict.values())
#     print "longest length is: " + str(longest_len)

#     word_count = sorted(string_dict.values())
#     # print "sorted list of word counts: " + str(word_count)
#     # print "sorted list by alphabetized keys: " + str(sorted(string_dict.items()))
#     # print "sorted list of alphabetized keys: " + str(sorted(string_dict.keys()))
#     max_value = max(map(int, string_dict.values()))
#     # print "max_length: " + str(max_value)

#     for word, length in string_dict.iteritems():
#         if max_value == length:
#             print word
#             print "list: ", list(string_dict.keys())[list(string_dict.values()).index(length)]
 

def longest_consec(strarr, k):
    longest_str = ''
    k =  k - 1
    length = 0
    i = 0
    
    while i < len(strarr) - k:
        current_longest = list()
        num_words = 0
        while num_words <= k:
            current_longest.append(strarr[i + num_words])
            num_words = num_words + 1

        current_word = ''.join(current_longest)
        if len(current_word) > length:
            length = len(current_word)
            longest_str = current_word
        i = i + 1
    return ''.join(longest_str)
    
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"],2)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "SUCCESS!"
