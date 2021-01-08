"""
The Secondary and Tertiary Structures of DNA

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string ss is the string scsc formed by reversing the symbols of ss, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string ss of length at most 1000 bp.

Return: The reverse complement scsc of ss.

>>> dna_complements('AAAACCCGGT')
'ACCGGGTTTT'

"""

def dna_complements(dna):

	dna_complement = dna.replace('A', 'C')

	return dna_complement


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"  