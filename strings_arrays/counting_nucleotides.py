"""
A Rapid Introduction to Molecular Biology

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string ss of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.

Sample Dataset

>>> count_nt("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
'20 12 21 17'

"""

def count_nt(nt_str):
	nt_dict = {
				'A':0,
				'C':0,
				'T':0,
				'G':0
	}


	for nt in list(nt_str):
		if nt in nt_dict:
			nt_dict[nt] += 1

	res = ' '.join(str(val) for val in nt_dict.values())
	
	return res

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"  