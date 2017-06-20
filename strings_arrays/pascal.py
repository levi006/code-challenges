from pprint import pprint 

"""
Pascal's Triangle 

Every number in Pascal's triangle is defined as the sum of the item above it and the item directly to
upper left of it. If there is a position that does not have an entry, we treat it as if we had a 0 there 


Item:   0  1  2  3  4  5
Row 0:  1
Row 1:  1  1
Row 2:  1  2  1
Row 3:  1  3  3  1
Row 4:  1  4  6  4  1
Row 5:  1  5 10 10  5  1
"""

def pascal(row, column):
    """
    >>> pascal(0, 0)
    1
    >>> pascal(5, 4)
    5
    >>> pascal(0, 1)
    0
    >>> pascal(1, 5)
    0
    """
    if column == 0:
        return 1
    elif row == 0:
        return 0
    else:
        return pascal(row-1, column) + pascal(row-1, column-1)

def P(n,r):

    if n == 0:
        return 1
    elif r == 0:
        return 0
    return P(n-1, r-1) + P(n-1, r)

print(P(0,1))



def generate(numRows):
    triangles = []
    for i in range(numRows):
        triangles.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                triangles[i].append(1)
            else:
                triangles[i].append(triangles[i - 1][j - 1] + triangles[i - 1][j])
    return triangles

pprint(generate(5))

def getRow(rowIndex):
    result = [1]
    for i in range(1, rowIndex + 1):
        result = [1] + [result[j - 1] + result[j] for j in range(1, i)] + [1]
    return result

pprint(getRow(5))



def triangle(n, lol=None):
    if lol is None: lol = [[1]]
    if n == 1:
        return lol
    else:
        prev_row = lol[-1]
        new_row = [1] + [sum(i) for i in zip(prev_row, prev_row[1:])] + [1]
        return triangle(n - 1, lol + [new_row])

pprint(triangle(5))
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"
