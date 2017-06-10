from pprint import pprint

# Given a 2D integer array representing a completely filled sudoku puzzle, implement a function which validates the puzzle according to the 3 rules:
# 1) Every row must contain all integer values 1-9 once and only once
# 2) Every column must contain all integer values 1-9 once and only once
# 3) Every 3x3 subsquare must contain all integer values 1-9 once and only once

matrix_valid = [

[5,1,3,6,8,7,2,4,9],
[8,4,9,5,2,1,6,3,7],
[2,6,7,3,4,9,5,8,1],
[1,5,8,4,6,3,9,7,2],
[9,7,4,2,1,8,3,6,5],
[3,2,6,7,9,5,4,1,8],
[7,8,2,9,3,4,1,5,6],
[6,3,5,1,7,2,8,9,4],
[4,9,1,8,5,6,7,2,3]

]

matrix_invalid = [

[5,1,3,6,8,7,2,4,9],
[8,4,9,5,2,1,6,3,7],
[2,6,7,3,4,9,5,8,1],
[1,5,8,4,6,3,9,7,2],
[9,7,4,2,1,8,3,6,5],
[3,2,6,7,9,5,4,1,8],
[7,8,2,9,3,4,1,5,6],
[6,3,5,1,7,2,8,9,4],
[1,9,1,8,5,6,7,2,3]

]

def main(matrix):
    """
    >>> main(matrix_valid)
    True

    >>> main(matrix_invalid)
    False

    """
    for row in matrix:
        check_sudoku(row)
    for col in matrix:
        check_sudoku(col)
    check_subsquare(matrix)
    pprint(matrix)


def check_sudoku(arr):
    """
    >>> check_sudoku([5,1,3,6,8,7,2,4,9])
    True

    >>> check_sudoku([5,1,3,6,8,7,2,4,9])
    True

    >>> check_sudoku([1,9,1,8,5,6,7,2,3])
    False

    """
    
    valid = {1,2,3,4,5,6,7,8,9}
    
    if set(arr) == valid:
        return True
    else:
        return False

def get_columns(matrix):
    """
    >>> get_columns([[1,2,3],[4,5,6],[7,8,9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    """
    columns = []
    for i in range(len(matrix)):
        column = [row[i] for row in matrix]
        columns.append(column)        
    return columns
    
def get_subsquares(matrix):
    """
    >>> get_subsquares([[5,1,3,6,8,7,2,4,9],[8,4,9,5,2,1,6,3,7],[2,6,7,3,4,9,5,8,1],[1,5,8,4,6,3,9,7,2],[9,7,4,2,1,8,3,6,5],[3,2,6,7,9,5,4,1,8],[7,8,2,9,3,4,1,5,6],[6,3,5,1,7,2,8,9,4],[4,9,1,8,5,6,7,2,3]])
    [[[5, 1, 3], [8, 4, 9], [2, 6, 7]], [[6, 8, 7], [5, 2, 1], [3, 4, 9]], [[2, 4, 9], [6, 3, 7], [5, 8, 1]], [[1, 5, 8], [9, 7, 4], [3, 2, 6]], [[4, 6, 3], [2, 1, 8], [7, 9, 5]], [[9, 7, 2], [3, 6, 5], [4, 1, 8]], [[7, 8, 2], [6, 3, 5], [4, 9, 1]], [[9, 3, 4], [1, 7, 2], [8, 5, 6]], [[1, 5, 6], [8, 9, 4], [7, 2, 3]]]

    """
    s_squares = []
    for i_c in range(0, 9, 3):
        for i_r in range(0, 9, 3):
            s_square = list(row[i_r: i_r + 3] for row in matrix[i_c:i_c + 3])
            s_squares.append(s_square)
    return s_squares

def check_subsquare(matrix):
    flat_squares = []
    s_squares = get_subsquares(matrix)

    for square in s_squares:
        flat_square = [item for b in square for item in b]
        check_sudoku(flat_square)
    
def main(matrix):
    """
    >>> main(matrix_invalid)
    False

    >>> main(matrix_valid)
    True

    """
    for r in matrix:
        check_sudoku(r)
    for c in matrix:
        check_sudoku(c)
    check_subsquare(matrix)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"  