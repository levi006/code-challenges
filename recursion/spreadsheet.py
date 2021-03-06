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

# content = r2c0 + r1c0 => 4 + 2 = 6

# smallest problem = evaluating a single cell + the rest of the cells in the calculation 

# base case  =  cell only contains an integer

# r2c0 = r1c1 + 2 => 8 + 2 = 10 
# r1c1 = r0c2 + 2 => 8 
# r0c2 + 2 => 4 + 2

input_arr = [
    ["1",      "r0c0",   "4"     ],
    ["r0c1+1", "r0c2+2", "5"     ],
    ["r1c1+2", "r2c0+r1c0", "r0c2+1"],
]
# In the example above, calculate_value(2, 1) yields 10.

#tail recursion
#start = list_of_cells[0] 
#rest_of cells = list_of_cells[1:]
#cell_contents = integer, integer + rc, rc + rc 



# def calculate_value(r,c):

#     total = 0
#     # print total, "start total" 
#     if input_arr[r][c].isdigit() == True: 
#         total = total + int(input_arr[r][c]) 
#         # print total, "integer cell"
#         # return total

#     if type(input_arr[r][c]) == str:
#         cells = input_arr[r][c].split("+")
#         # print cells, "cells"
#         for cell in cells:
#             if cell.isdigit() == True:
#                 total = total + int(cell)
#                 # print cell, "integer cell"
#                 # print total, "running total"
#             else:
#                 # print cell
#                 r = int(cell[1])
#                 c = int(cell[3])
#                 calculate_value(r,c)
#         # print total, "end total"
#         return total



def calculate_value(r,c):
    cell = int(input_arr[r][c]) 
 
    if cell.isdigit(): 
        return cell

    else:  
        cells = input_arr[r][c].split("+")
        
        for cell in cells:
            if "+" not in cell:
                      
                r = int(cell[1])
                c = int(cell[3])
                return calculate_value(r,c)

print calculate_value(2,1)

            





