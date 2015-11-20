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

#Sort and Compare: 

#Anagrams are anagrams if they consist of exactly the same characters. 
#Sort each string alphabetically, from A to Z. If the two strings are equal, then they're anagrams. 
#Python sort method is O(n^2) or O(nlogn), so this algorithm will have the same runtime as the sorting process.

def anagramSolution2(s1,s2):
	alist1 = list(s1) 
	alist2 = list(s2)

	alist1.sort()
	alist2.sort()

	pos = 0
	matches = True

	while pos < len(s1) and matches:
		if alist1[pos]==alist2[pos]:
			pos = pos + 1
		else:
			matches = False 

	return matches 	


#Count and Compare

#Any two anagrams will have the same number of a's, b's, c's, etc. 
#To decide if two strings are anagrams, count the number of times a character occurs. 
#Use 26 counters for each possible character. 
#If the two lists are identical at the end, the strings are anagrams. 

def anagramSolution3(s1,s2):
	c1 = [0]*26
	c2 = [0]*26

	for i in range(len(s1)):
		pos = ord()

