def insert_commas(number):
	number_list = list(str(number.split(""))
	for i in range(len(number_list))[::-3][1::]
    	number_list.insert(i+1,",")
	result = "".join(number_list)
	print result
insert_commas(1000000)

