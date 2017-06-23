import csv
import re
import datetime

def fix_acct_num(acct_num):
    """Fix account number: ensure it padded with zeroes to length of 6.
    
        >>> fix_acct_num("123456")
        '123456'

        >>> fix_acct_num("123")
        '000123'

        >>> fix_acct_num("ABC123")
        Traceback (most recent call last):
            ...
        ValueError: Invalid account num: ABC123
    """


    if not acct_num.isdigit():
        raise ValueError("Invalid account num: " + acct_num)

    if len(acct_num) < 6:
        acct_num = "%06d" % int(acct_num)

    return acct_num

def fix_date(date):
    """Fix date: reformat 'Dec 1 2017' => '20171201'
    
        >>> fix_date('Dec 1 2017')
        '20171201'

        >>> fix_date('Dec 32 2017')
        Traceback (most recent call last):
            ...
        ValueError: time data 'Dec 32 2017' does not match format '%b %d %Y'
    """

    date = datetime.datetime.strptime(date, "%b %d %Y").strftime("%Y%m%d")

    return date

def fix_address(address):
    """No cleanup needed for address.
    
        >>> fix_address('123 Main Street')
        '123 Main Street'
    """

    address = address.strip()

    return address

def fix_zipcode(zipcode):
    """Zipcodes less than 5 digits long are padded with leading zeros. 

        >>> fix_zipcode('12345')
        '12345'

        >>> fix_zipcode('123')
        '00123'

        >>> fix_zipcode('ABCDE')
        Traceback (most recent call last):
            ...
        ValueError: Invalid zipcode: ABCDE
    """

    if not zipcode.isdigit():
        raise ValueError("Invalid zipcode: " + zipcode)

    if len(zipcode) < 5:
        zipcode = "%05d" % int(zipcode)

    return zipcode

def fix_consumption(consumption):
    """Validate consumption.

    Return an integer, removing commas if present:

        >>> fix_consumption('123')
        123

        >>> fix_consumption('1,213')
        1213

    Interpret a (number) as negative:

        >>> fix_consumption('(123)')
        -123

        >>> fix_consumption('(1,213)')
        -1213

    Return error if invalid:

        >>> fix_consumption('ABC')
        Traceback (most recent call last):
            ...
        ValueError: Invalid consumption: ABC

        >>> fix_consumption('(123')  # no closing paren
        Traceback (most recent call last):
            ...
        ValueError: Invalid consumption: (123
    """
    
    if consumption[0] == "(" and consumption[-1] == ")":
        consumption = consumption[1:-1]
        sign = -1

    else:
        sign = +1

    consumption = consumption.replace(",", "")

    if not consumption.isdigit():
        raise ValueError("Invalid consumption: " + consumption)

    return int(consumption) * sign

		
def extract_line_to_row(line):
    """Process a line of input in a row of data.

        >>> extract_line_to_row(
        ...     "81769 Feb 25 2017    25 California Way      94111     105  ")
        ['081769', '20170225', '25 California Way', '94111', 105]

    """
    # defining columns in fixed width input file
    acct_num = line[0:6].strip()
    date = line[6:17].strip()
    address = line[21:44].strip()
    zipcode = line[44:49].strip()
    consumption = line[54:].strip()

    # normalizing functions for each column 
    acct_num = fix_acct_num(acct_num)
    read_date = fix_date(date)
    address = fix_address(address)
    zipcode = fix_zipcode(zipcode)
    consumption = fix_consumption(consumption)

    new_row = [acct_num, read_date, address, zipcode, consumption]

    return new_row

def process_file(in_file, out_file, dupe_file):
    """Process CSV file, writing CSV output and duplicate-record output."""    
    
    headers = ['Account', 'Read Date', 'Address', 'Zip Code', 'Consumption']

    with open(in_file, 'r') as txt_file, \
         open(out_file, 'w') as csv_file, \
         open(dupe_file, 'w') as dupe_file:

        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        writer.writerow(headers)

        dupe_writer = csv.writer(dupe_file, delimiter=',', lineterminator='\n')
        dupe_writer.writerow(headers)
        
        possible_dupes = set()

        for line in txt_file:

            data = extract_line_to_row(line)
    		
            # records with the same account number and read date are logged as possible duplicates
            key = (data[0], data[1])

            if key not in possible_dupes:
            	possible_dupes.add(key)
                writer.writerow(data)

            # possible duplicates are written out to a csv file
            else:
                dupe_writer.writerow(data)


process_file("example_input.txt", "transformed.csv", "dupes.csv")		

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"

		
