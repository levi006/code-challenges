import math
def standard_deviation(number_list):
 
    average = sum(number_list) / float(len(number_list))
     
    stdev = 0
    for value in number_list:
        stdev += math.sqrt((average - value)**2) / float(len(number_list))
     
    return stdev

def stddev(number_list):
 
    average = sum(number_list) / float(len(number_list))
     
    variance = 0
    for value in number_list:
        variance += ((average - value)**2) / float(len(number_list))
    stddev = math.sqrt(variance)
    return stddev

print(standard_deviation([1,2,3,4,5]))
print(stddev([1,2,3,4,5]))