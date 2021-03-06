"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

>>> high_and_low("1 2 3 4 5")
'5 1'

>>> high_and_low("1 2 -3 4 5")
'5 -3'

>>> high_and_low("1 9 3 4 -5")
'9 -5'

>>> high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
'542 -214'

Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.

"""
# def high_and_low(numbers):
#     number_list = numbers.strip().split()
#     integer_list = map(int, number_list)
#     # print integer_list
#     # print type(integer_list)
    
#     high = integer_list[0]
#     low = integer_list[0]
    
#     for num in range(len(integer_list)):
#         if integer_list[num] < low:
#             low = integer_list[num]
#         if integer_list[num] > high:
#             high = integer_list[num]

#         high_low = str(high), str(low)
#         numbers = " ".join(high_low)
#         # print repr(numbers)
#         # print type(numbers)    
#     return numbers

def high_and_low(numbers):
    string_list = numbers.strip().split()
    
    int_list = []

    for i in range(len(string_list)):
        int_list.append(int(string_list[i]))
    return str(max(int_list)) + " " + str(min(int_list))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "SUCCESS!"