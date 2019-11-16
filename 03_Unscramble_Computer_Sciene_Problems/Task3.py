"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#=========================# PART A #=========================#
def get_telephone_type(tel_num):
	if tel_num.startswith('(0') and tel_num.find(')'):
		return 'Fixed'
	elif (tel_num.startswith('7') or tel_num.startswith('8') or tel_num.startswith('9')) and ' ' in tel_num:
		return 'Mobile'
	elif (tel_num.startswith('140')):
		return 'Telemarketers'
	else:
		return None

def extract_area_code(tel_num, tel_type):
	if tel_type == 'Fixed':
		return tel_num[1:tel_num.find(')')]
	elif tel_type == 'Mobile':
		return tel_num[0:4]
	elif tel_type == 'Telemarketers':
		return '140'
	else:
		return None

def extract_receiver_area_codes(calls, caller_prefix, duplicates = False):
	area_codes = []
	for call in calls:
		if call[0].startswith(f"{caller_prefix}"):
			tel_type = get_telephone_type(call[1])
			area_code = extract_area_code(call[1], tel_type)
			if area_code:
				if duplicates:
					area_codes.append(area_code)
				else:
					if area_code not in area_codes:
						area_codes.append(area_code)
	return area_codes

print(f"The numbers called by people in Bangalore have codes: {extract_receiver_area_codes(calls,'(080)')}")

#=========================# PART B #=========================#

def get_number_of_calls(calls, caller_prefix, receiver_area_code):
  number_of_calls = 0
  area_codes = extract_receiver_area_codes(calls, caller_prefix, duplicates=True)
  for area_code in area_codes:
    if area_code == receiver_area_code:
      number_of_calls += 1
  return (number_of_calls, len(area_codes)) # tuple returned (number of calls for specific area code, total number of calls)

def calc_percentage(ratio):
  return round(ratio[0] / ratio[1] *100, 2)

def get_percentage_of_calls(calls, caller_prefix, receiver_area_code):
  return calc_percentage(get_number_of_calls(calls, caller_prefix, receiver_area_code))

print(f"{get_percentage_of_calls(calls, '(080)', '080')} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
