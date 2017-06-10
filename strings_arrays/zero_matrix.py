Skip to content
This repository
Search
Pull requests
Issues
Marketplace
Gist
 @levi006
 Sign out
 Watch 1
  Star 7
  Fork 2 theresa-clare/Code-Challenges
 Code  Issues 0  Pull requests 0  Projects 0  Wiki Insights 
Branch: master Find file Copy pathCode-Challenges/arrays-and-strings/zero_matrix.py
0ccd172  on Sep 24, 2015
@theresa-clare theresa-clare Placed files into folders based on category
1 contributor
RawBlameHistory     
54 lines (45 sloc)  1.67 KB
#########################################################################################
# 					Exercise 1.7 of Cracking the Coding Interview v5					#
#																						#
# Write an algorithm such that if an element in an M x N matrix is 0, its entire row 	#
# and column are set to 0. 																#
#########################################################################################

def get_zeros(matrix):
	"""
	Traverses matrix and returns list of coordinates of zeros
	>>> get_zeros([[1, 0, 3, 4, 5], [6, 7, 0, 9, 10], [1, 2, 3, 4, 5]])
	[[0, 1], [1, 2]]
	"""
	zero_coordinates = []
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 0:
				zero_coordinates.append([row, col])
	return zero_coordinates

def set_zeros(matrix, zero_coordinate):
	"""
	Given a coordinate, set that coordinate's row and column to 0
	>>> set_zeros([[1, 0, 3, 4, 5], [6, 7, 0, 9, 10], [1, 2, 3, 4, 5]], [0,1])
	[[0, 0, 0, 0, 0], [6, 0, 0, 9, 10], [1, 0, 3, 4, 5]]
	"""
	# zero out row
	matrix[zero_coordinate[0]] = [0]*len(matrix[zero_coordinate[0]])
	# zero out column
	for row in matrix:
		row[zero_coordinate[1]] = 0
	return matrix

def row_column_zero(matrix):
	"""
	Given a matrix, sets row and column to 0 for all elements equaling to 0
	and returns zeroed matrix
	>>> row_column_zero([[1, 0, 3, 4, 5], [6, 7, 0, 9, 10], [1, 2, 3, 4, 5]])
	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 4, 5]]
	"""
	zeros = get_zeros(matrix)
	for coordinate in zeros:
		new_matrix = set_zeros(matrix, coordinate)
	return new_matrix


#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help