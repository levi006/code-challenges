def narcissistic( value ):
    if value < 10:
        return True
    
    str_nums = str(value)
    
    total = 0
    power = len(str_nums)
    for num in str_nums:
        total = int(num)**power + total

    if total == value:
        return True
    else:
        return False