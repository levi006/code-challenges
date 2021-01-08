# Simple Spreadsheet
#
# Given an M x N grid, the content of each cell can be:
#
# - A positive integer number.
#   E.g., 3, 15
# or
# - A cell reference of format: rXcY.
#   E.g., r0c3, r2c1
# or
# - An expression of X + Y (where X and Y can be either a number or a cell reference)
#   E.g., r1c2 + 1, 2 + 5, r1c2 + r1c2, r2c1 + r3c5
#
#        c0        c1        c2
#    +---------+------------+---------+
# r0 + 1       |  r0c0      +   4     |
#    +---------+------------+---------+
# r1 + r0c1 + 1| r0c2 + 2   |   5     |
#    +---------+------------+---------+
# r2 + r1c1 + 2| r2c0 + r1c0| r0c2 + 1|
#    +---------+------------+---------+
#
# Write a function to calculate the value for any given cell.
#
# The function takes the signature: calculate_value(r, c)
# and returns an integer.
#
# The input is a 2 dimensional array of M rows and N columns each row
# and the content of each cell is a string.

# row = 2, 
# column = 1

# r2c0 = r1c1 + 2 => 8 + 2 = 10 
# r1c1 = r0c2 + 2 => 8 
# r0c2 + 2 => 4 + 2

# smallest problem = evaluating a single cell + the rest of the cells in the calculation 
# base case  =  cell only contains an integer
# cell_contents = integer, integer + rc, rc + rc 

# input_arr = [
#     ["1",      "r0c0",   "4"     ],
#     ["r0c1+1", "r0c2+2", "5"     ],
#     ["r1c1+2", "r2c0+r1c0", "r0c2+1"],
# ]
# In the example above, calculate_value(2, 1) yields 10.

# What if there was a circular reference?

#        c0        c1        c2
#    +---------+------------+---------+
# r0 + 1       |  r2c0      +   4     |
#    +---------+------------+---------+
# r1 + r0c1 + 1| r0c2 + 2   |   5     |
#    +---------+------------+---------+
# r2 + r0c1    | r2c0 + r1c0| r0c2 + 1|
#    +---------+------------+---------+

circ_arr = [
    ["1",      "r2c0",   "4"     ],
    ["r0c1+1", "r0c2+2", "5"     ],
    ["r0c1", "r2c0+r1c0", "r0c2+1"],
]

# r2c0 -> r0c1 and at the same time r0c1 -> r2c
# calculating the value of a cell creates an infinite recursion loop
# need to check if a cell is pointing to another cell and raise error if loop is found
# similar to finding a loop in a linked list; each cell is a node
 
def calculate_value(r,c):
    cell = circ_arr[r][c]
    print(cell), "cell"

    # cell contains a number
    if cell.isdigit():
        return int(cell)

    # cell contains a single r,c reference
    if "+" not in cell:
        r = int(cell.split("c")[0][1:])
        c = int(cell.split("c")[1])
        print r,c, "r,c"

        return calculate_value(r,c)

    # cell contains (r,c + r,c) or (r,c + num) references
    a,b = cell.split("+")

    if a.isdigit():
        a = int(a)

    else:
        r = int(str(a.split("c")[0][1:]))
        c = int(a.split("c")[1])
        a = calculate_value(r,c)

    if b.isdigit():
        b = int(b)

    else:
        r = int(b.split("c")[0][1:])
        c = int(b.split("c")[1])
        b = calculate_value(r,c)

    return a + b 

print calculate_value(2,1)



