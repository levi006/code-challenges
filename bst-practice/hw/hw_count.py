"""How many nodes in a binary tree?"""

from bst import bst


def count(node):
    """How many nodes in a BST?

        >>> count(bst)
        8
    """
    if node is None:
        return 0
    
    else:
        return 1 + count(node.left) + count(node.right)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"
