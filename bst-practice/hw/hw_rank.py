"""Find rank of node in binary search tree."""

from bst import bst


def rank(node, val):
    """Return rank (root is 0) of node with val (recursive).

        >>> rank(bst, 5)
        0

        >>> rank(bst, 7)
        1

        >>> rank(bst, 1)
        2
    """

    rank = 0 

    while node is not None:
        if node.data == val:
            return rank

        if node.data > val:
            node = node.left

        else:
            node = node.right

        rank = rank + 1


def rrank(node, val):
    """Return rank (root is 0) of node with val (recursive).

        >>> rrank(bst, 5)
        0

        >>> rrank(bst, 7)
        1

        >>> rrank(bst, 1)
        2
    """
    if node is None:
        return None

    if node.data == val:
        return 0

    if val < node.data:
        return rank(node.left, val) + 1

    else:
        return rank(node.right, val) + 1

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"


