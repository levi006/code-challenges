"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

>>> tower_builder(1)
['*']

>>> tower_builder(2)
[' * ', '***']

>>> tower_builder(3)
['  *  ', ' *** ', '*****']

"""

def tower_builder(n_floors):
    tower = []
    indent = " "
    n = n_floors
    for i in range(n_floors):
        n = n -1
        # print(n)
        floor = indent*(n) + "*"*((i*2)+1) + indent*(n)
        tower.append(floor)
#         print(tower)
    return tower


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"