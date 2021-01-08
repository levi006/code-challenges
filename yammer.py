

#
# Given a positive integer N, return the Nth fibonacci number
# f[1] = 0, f[2] = 1, f[n] = f[n-1] + f[n-2]
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 
#
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib((n-2)) + fib((n-1))
        
    
'''
 You are given the following 3-by-3 grid matrix, where the zeros are vertices
 and the bars/lines are edges (i.e. a link between vertices):
 0-0-0
 | | |
 0-0-0
 | | |
 0-0-0
 Enumerate all paths that start in the upper left vertex and, moving only
 right (R) and down (D), end in the bottom right vertex. One such path
 is "RRDD", another is "RDRD". Your solution should solve the 3-by-3 case,
 but should also generalize to N-by-N matrices/grids:
 ["RRDD", "RDRD", "DDRR", ...]
'''
# public List<string> enumeratePaths(int N) {
# }
def enumeratePaths(n):
    all_paths = []
    current_path = ""
    downMoves = n - 1
    rightMoves = n - 1
    enumPathsHelper(all_paths, current_path, downMoves, rightMoves)
    return all_paths
    
    
def enumPathsHelper(all_paths, current_path, downMoves, rightMoves):
    if downMoves == 0 and rightMoves == 0:
        all_paths.append(current_path)
        return
    if rightMoves > 0:
        enumPathsHelper(all_paths, current_path + "R", downMoves, rightMoves - 1)
    if downMoves > 0:
        enumPathsHelper(all_paths, current_path + "D", downMoves - 1, rightMoves)
        

def main():
    print(enumeratePaths(5))
    print(len(enumeratePaths(5)))

if  __name__ =='__main__':main()