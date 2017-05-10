"""Find height of a binary tree."""

from bst import bst

#the height of a tree is 1 + the height of the rest of the tree
def height(node):
    """Find height of tree.

        >>> height(bst)
        4
    """
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)


    return 1 + max(left_height, right_height)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"

