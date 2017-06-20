def two_sum(nums, target):   
    map = {}
    for i in range(len(nums)):
        if nums[i] not in map:
            map[target - nums[i]] = i 
            print map
        else:
            return map[nums[i]], i
        print map

    return -1, -1

print two_sum([2,7,11,15], 9)
