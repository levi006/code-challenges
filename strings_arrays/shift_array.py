def shift_array(lst, k):
    """
    >>> shift_array([1,2,3,4,5], 2)
    [3, 4, 5, 1, 2]

    >>> shift_array([1,2,3], 4)
    []

    >>> shift_left([1,2,3,4,5], 2)
    [3, 4, 5, 1, 2]
    """

    if len(lst) < k:
        return []

    temp = lst[0]

    for i in range(len(lst) - k):
        curr_index = i
        new_index = i - k

        if new_index < 0:
            new_index = (len(lst) - 1) - abs(i) 
        
        lst[curr_index] = lst[new_index]
        print lst
    
        curr_index += 1



    # lst[curr_index] = temp 
    return lst

def shift_left(lst, k):
    temp = lst[0]
    for index in range(len(lst) - k):
        lst[index] = lst[index + k]         
    lst[index + k] = temp
    return lst


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"

