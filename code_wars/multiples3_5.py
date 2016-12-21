def solution(number):
    
    multiples = []

    for i in range(number):
        print number 
        if number%3 == 0 or number%5 == 0:
            print number%3
            print number%5
            multiples.append(number)
            print multiples

        # if number%3 and number%5 == 0 and number not in multiples:
        #     multiples.append(number)
        #     print multiples    
      
    # for i in range(len(multiples)):
    #     sum = []
    #     sum = sum[i]*sum[i+1]
    #     print sum 
    # return

solution(10)