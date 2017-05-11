"""
Find the max sum of any two contiguous numbers in a given array. 
>>> max_subarray([2,3,1,2,4,3])
7

>>> max_subarray([2,3,1,-4,2,4])
6

>>> max_subarray([])
0

>>> max_subarray([6,3,1,-4,2,4,10])
14

>>> max_subarray([2,3,10,1,-4,2,4])
13
"""
def max_subarray(nums):
    
    if nums == []:
        return 0
    else:
        curr_max = 0
        for i in range(1,len(nums)):
            first = nums[i-1]
            # print(first, "first")
            second = nums[i]
            # print(second, "second)")
            sub_array = first + second
            # print(sub_array, "subarray")
            
            if sub_array > curr_max:
                curr_max = sub_array
                # print(curr_max, "curr_max")
            else: 
                continue
    return curr_max 
            

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"