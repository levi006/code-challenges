"""Create a balanced BST."""

from bst import BNode

def create(nums):
    """Create a balanced BST.

        >>> bst = create([1, 2, 3, 4, 5, 6, 7])
        >>> bst.data
        4
        >>> bst.left.data
        2
        >>> bst.right.data
        6
    """

    if not nums:
        return 0

    midpt = len(nums) / 2

    mid = BNode(nums[midpt])
    mid.left = create(nums[0:midpt])
    mid.right = create(nums[midpt + 1:])

    return mid 


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"
