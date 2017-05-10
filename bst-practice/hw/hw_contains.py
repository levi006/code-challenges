"""Does binary search tree contain node?"""

from bst import bst

def contains(node, val):
    """Does tree starting at node contain node with val?

        >>> contains(bst, 5)
        True

        >>> contains(bst, 1)
        True

        >>> contains(bst, 2)
        False

        >>> contains(bst, 6)
        True
    """
    while node is not None:
        if  val == node.data:
            return True
        
        else:
            if val > node.data:
                node = node.right

            elif  val < node.data:
                node = node.left
    
    return False



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"