"""Is a BST valid?

A valid BST follows a left-is-less, right-is-greater rule.
"""

from bst import bst, BNode as N

def is_valid(node):
    """Is this node valid?

        >>> is_valid(bst)
        True

        >>> is_valid(N(2, N(1)))
        True

        >>> is_valid(N(1, N(2)))
        False

        >>> is_valid(N(4, N(2, N(1), N(3)), N(6, N(5), N(7))))
        True

        >>> is_valid(N(4, N(2, N(99), N(3)), N(6, N(5), N(7))))
        False
    """

    return ok(node, None, None)


def ok(node, minv, maxv):
    """Does this node fall within legal values?"""

    if node is None:
        return True 

    if ((node.data > maxv) and maxv is not None) or ((node.data < minv) and minv is not None):
        return False

    return ok(node.left, minv, node.data) and ok(node.right, node.data, maxv)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"
