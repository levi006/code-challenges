
import csv, re, datetime

def get_acct_num(raw_num):

	acct_num = raw_num

	if len(acct_num) <= 6:
		valid_acct_num = "%06d" % int(acct_num)

	return valid_acct_num

def get_date(raw_date):

	stripped_date = raw_date.strip()
	valid_date = datetime.datetime.strptime(stripped_date, "%b %d %Y").strftime("%Y%m%d")

	return valid_date

def get_address(raw_address):

	address = raw_address.strip()

	return address

def get_zipcode(raw_zip):
	"""Zipcodes less than 5 digits long are padded with leading zeros. """
	
	zc = raw_zip.strip()

	if len(zc) <= 5:
		valid_zc = "%05d" % int(zc)

	return valid_zc

def get_consumption(raw_c):
	"""Values containing commas are treated as string literals."""
	
	c = raw_c.strip()
	if c.isdigit():
		valid_c = int(raw_c)
	else:
		
		sections = re.split('[^0-9]+', raw_c)
		
		num = " "
		
		for section in sections:
			if section.isdigit():
				num += section

		valid_c = int(num)

	return valid_c

# transforms fixed width input file into csv
with open('example_input.txt', 'r') as txt_file, open('transformed.csv', 'w') as csv_file:

	writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
	writer.writerow(('Account Number', 'Read Date', 'Address', 'Zip Code', 'Consumption'))
	
	possible_dupes = dict()

	for line in txt_file:
		
		# defines columns in fixed width input file
		raw_acct_num = line[0:6]
		raw_date = line[6:17]
		raw_address = line[21:44]
		raw_zip = line[44:49]
		raw_c = line[54:]
		
		# normalizes functions for each column 
		acct_num = get_acct_num(raw_acct_num)
		read_date = get_date(raw_date)
		address = get_address(raw_address)
		zip_code = get_zipcode(raw_zip)
		consumption = get_consumption(raw_c)

		new_row = [acct_num, read_date, address, zip_code, consumption]
		writer.writerow(new_row)

		# records with the same account number and read date are logged as possible duplicates
		key = (acct_num, read_date)

		if key not in possible_dupes:
			possible_dupes[key] = [new_row]
		
		elif key in possible_dupes:
			possible_dupes[key].append(new_row)

# possible duplicates are written out to a csv file
with open('duplicates.csv', 'w') as dupes:

	dupe_writer = csv.writer(dupes, delimiter=',', lineterminator='\n')
	dupe_writer.writerow(('Account Number', 'Read Date', 'Address', 'Zip Code', 'Consumption'))
	for key in possible_dupes:
		if len(possible_dupes[key]) > 1:
			dupe_writer.writerows(possible_dupes[key])
			


		

		
