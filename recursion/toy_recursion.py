"""
>>> sum([10, -10, 36, 3])
39
    
>>> len('orange')
6

>>> largest_num([4,7,2,8])
8

>>> smallest_num([62, 4, 9, 23])
4

>>> flatten([1, [2, 3, [4]], 5, [[6]]]) 
[1, 2, 3, 4, 5, 6]

>>> fib_recurse(9)
34

"""
# the sum of a list is the first number + the sum of the smaller list
def sum(num_lst): 
    if num_lst == []:
        return 0
    else:
        first = num_lst[0]
        rest = num_lst[1:] 
        return first + sum(rest)

# the length of a string is 1 + the length of the shorter string 
def slen(string):
    if string == '':
        return 0
    else:
        return 1 + slen(string[1:])

# the largest number in a list is the largest number between the first number and the rest of the smaller list
def largest_num(num_lst):
    if num_lst == []:
        return 0
    else:
      first = num_lst[0]
      rest = num_lst[1:]
      return max(first, largest_num(rest)) 

def smallest_num(num_lst):
    if len(num_lst) == 1:
        return num_lst[0]
    else:
      first = num_lst[0]
      rest = num_lst[1:]
      return min(first, smallest_num(rest)) 

# a flattened list is a flattened list plus a list of other flattened lists
def flatten(lists):
  if isinstance(lists, list):
      if len(lists) == 0:
          return []
      first = lists[0]
      rest = lists[1:]
      # print("first: ", first, "rest: ", rest)
      return flatten(first) + flatten(rest)
  else:
      return [lists]

def fib_recurse(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib_recurse(n-1) + fib_recurse(n-2)
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"