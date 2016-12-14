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
	# print str(string_dict)
	
	longest_len = max(string_dict.values())
	print "longest length is " + str(longest_len)

	# print string_dict.keys() 

	#list of word lengths, sorted min to max
	word_count = sorted(string_dict.values())
	print string_dict.items()
	print max(string_dict[i][1].items())

	# for i in range(k):
	# 	concat_str = ''
	# 	''.join(word_count[::-1])
	# return concat_str
	
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"],2)