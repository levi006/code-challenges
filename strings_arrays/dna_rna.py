"""
The Second Nucleic Acid

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string tt corresponding to a coding strand, its transcribed RNA string uu is formed by replacing all occurrences of 'T' in tt with 'U' in uu.

Given: A DNA string tt having length at most 1000 nt.

Return: The transcribed RNA string of tt.

>>> tt("GATGGAACTTGACTACGTAAATT")
'GAUGGAACUUGACUACGUAAAUU'

"""

def tt(dna):

	rna = dna.replace('T', 'U')

	return rna


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"  