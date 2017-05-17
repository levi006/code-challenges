def narcissistic(value):
    str_nums = str(value)
    
    total = 0
    power = len(str_nums)
    for num in str_nums:
        total = int(num)**power + total

    return total == value

print narcissistic(7)
print narcissistic(371)
print narcissistic(122)
print narcissistic(4887)