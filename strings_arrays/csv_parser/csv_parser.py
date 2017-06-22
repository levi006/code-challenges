# 80 char
# doc string

# use fixed width, then line slicing
# (121), negative
# 1,232 or 1 or 232
# do we have dupes?


# A customer gives you a fixed-width input file (reference: example_input.txt).  You look at the file, and realize that while it has all the data you requested in the correct order, it does not meet your data specification and requires a data transformation. Please write a script or function that takes an input file in the sample format, and writes an output file matching the following specification:

# File must be in valid CSV format
# File must not contain duplicate rows
# File must contain a header row with column names
# Column 1: Account Number. If less than six digits, padded with leading zeroes
# Column 2: Read Date. Format: YYYYMMDD
# Column 3: Address (free text)
# Column 4: Zip Code. Five-digit format
# Column 5: Consumption (numeric value)

# Example input:

# 81769 Feb 25 2017	25 California Way	  94111	 105  
# 81723 Feb 26 2017	30 Water Way, C/O James94103	 102  
# 45	Mar 18 2017	15 Chesterfield Place  1012	  1,232 
# 571872Mar 15 2017	20 Amherst Street	  1003	  113  
# 45	Mar 18 2017	15 Chesterfield Place  1012	  123  
# 1011  Sep 2 2016	 19 Amherst Street	  1003	  (121)


import csv, re, datetime

with open('example_input.txt', 'r') as txt_file, open('transformed.csv', 'w') as csv_file, open('dupes.csv', 'w') as dupes:
	reader = (row.strip().split() for row in txt_file)

	writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
	# dupes_writer = csv.writer(dupes, delimiter=',', lineterminator='\n')
	writer.writerow(('Account Number', 'Read Date', 'Address', 'Zip Code', 'Consumption'))

	# entries = set()

	for row in reader:

		raw_acct_num = row[0]
		raw_date = ' '.join(row[1:4])
		raw_address = ' '.join(row[4:-2])
		raw_zip = row[-2]
		raw_consumption = row[-1]

		# if row[0] in entries:
		# 	dupes_writer.writerow(row)
			
		# account number
		if raw_acct_num.isdigit() == False:
			sections = re.split('((?:^\s*-)?\d+)', raw_acct_num)
			for section in sections:
				if section.isdigit() == True:
					acct_num = section

				if section.isalpha():
					raw_date = section + " " + raw_date

		elif raw_acct_num.isdigit() and len(raw_acct_num) < 6:
			acct_num = "%06d" % int(raw_acct_num)

		else:
			acct_num = row[0]
			
		# date
		date_list = raw_date.split()

		# check YYYY length of MM DD YYYY format
		if len(date_list[-1]) != 4:
			extra = date_list.pop()
			raw_address = extra + " " + raw_address 

		read_date = "".join(date_list)

		parsed_date = datetime.datetime.strptime(read_date, "%b%d%Y").strftime("%Y%m%d")
		
		# zip code
		if raw_zip.isdigit() == False:
			sections = re.split('((?:^\s*-)?\d+)', raw_zip)
			
			for section in sections:
				if section.isdigit() == True:
					zip_code = section
				
				if section.isalpha():
					raw_address = raw_address + " " + section

		elif raw_zip.isdigit() and len(raw_zip) < 5:
			zip_code = "%05d" % int(raw_zip)
		
		else:
			zip_code = row[-2]

		# consumption
		if raw_consumption.isdigit():
			consumption = int(raw_consumption)

		else:
			sections = re.split('((?:^\s*-)?\d+)', raw_consumption)
			
			num = " "
			
			for section in sections:
				if section.isdigit():
					num += section

			consumption = int(num)

		# address
		address = raw_address
		
		new_row = [acct_num, parsed_date, address, zip_code, consumption]
		writer.writerow(new_row)









