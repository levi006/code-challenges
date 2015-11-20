#Checking if each character in the string occurs in the second string
#Because strings are immutable, each string will be converted into a list
#Each character will be checked off by replacing with "None"
#each of the n positions in a list for the second string will be visited once to match a character 
#Runtime is O(N^2) because the number of visits is equal to the sum fo the integers

#Checking Off: 

def anagramSolution(s1,s2):
	alist = list(s2)

	pos1 = 0 
	stillOK = True

	while pos1 < len(s1) and stillOK:
		pos2 = 0 
		found = False
		while pos2 < len(alist) and not found:
			if s1[pos1] == alist[pos2]:
				found = True
			else:
				pos2 = pos2 + 1

		if found:
			alist[pos2] = None
		else:
			stillOK = False

		pos1 = pos1 + 1

	return stillOK 