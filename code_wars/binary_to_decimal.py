def binary_array_to_number(arr):
    number = 0
    for i in range(len(arr)):
        number = number*2 + arr[i]
        print(number)
    return number 