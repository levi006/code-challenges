def  oddNumbers(l, r):
	odds = []
	for num in range(l, r+1):
		if num % 2 == 1:
			odds.append(num)
	print odds
	return odds

oddNumbers(3,9)
