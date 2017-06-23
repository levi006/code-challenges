
import csv, re, datetime

def fix_acct_num(acct_num):

	if len(acct_num) <= 6:
		acct_num = "%06d" % int(acct_num)

	return acct_num

def fix_date(date):

	stripped_date = date.strip()
	valid_date = datetime.datetime.strptime(stripped_date, "%b %d %Y").strftime("%Y%m%d")

	return valid_date

def fix_address(address):

	address = address.strip()

	return address

def fix_zipcode(zipcode):
	"""Zipcodes less than 5 digits long are padded with leading zeros. """
	
	zipcode = zipcode.strip()

	if len(zipcode) <= 5:
		zipcode = "%05d" % int(zipcode)

	return zipcode

def fix_consumption(consumption):
	"""Values containing commas are treated as string literals."""
	
	consumption = consumption.strip()
	if consumption.isdigit():
		consumption = int(consumption)
	else:
		
		sections = re.split('[^0-9]+', consumption)
		
		num = " "
		
		for section in sections:
			if section.isdigit():
				num += section

		consumption = int(num)

	return consumption

# transforms fixed width input file into csv
with open('example_input.txt', 'r') as txt_file, open('transformed.csv', 'w') as csv_file:

	writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
	writer.writerow(('Account Number', 'Read Date', 'Address', 'Zip Code', 'Consumption'))
	
	possible_dupes = dict()

	for line in txt_file:
		
		# defining columns in fixed width input file
		acct_num = line[0:6]
		date = line[6:17]
		address = line[21:44]
		zipcode = line[44:49]
		consumption = line[54:]
		
		# normalizing functions for each column 
		acct_num = fix_acct_num(acct_num)
		read_date = fix_date(date)
		address = fix_address(address)
		zipcode = fix_zipcode(zipcode)
		consumption = fix_consumption(consumption)

		new_row = [acct_num, read_date, address, zipcode, consumption]
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
			


		

		
