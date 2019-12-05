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

def get_telephone_type(number):
  if number.startswith('(0') and number.find(')'):
    return f'Fixed'
  elif number.startswith('7') or number.startswith('8') or number.startswith('9') and ' ' in number:
    return 'Mobile'
  elif number.startswith('140'):
    return 'Telemarketers'
  else:
    None

def extract_tel_code(number, teltype):
  if teltype == 'Fixed':
    return number[1:number.find(')')]
  elif teltype == 'Mobile':
    return number[0:4]
  elif teltype == "Telemarketers":
    return number[0:3]
  else:
    return None

# numbers = ['(022)47410783', '98459 20681', '1408371942']
# for num in numbers:
#   teltype = get_telephone_type(num)
#   print(extract_tel_code(num, teltype))

def extract_receiver_area_code(calls, caller_prefix):
  area_codes = []
  for call in calls:
    if call[0].startswith(f"{caller_prefix}"):
      get_type = get_telephone_type(call[1])
      extract_tel = extract_tel_code(call[1], get_type)
      if extract_tel not in area_codes:
        area_codes.append(extract_tel)
  return area_codes

print(extract_receiver_area_code(calls, '(080)'))

def count_in_state_calls(calls, caller_prefix):
  count = 0
  total = 0
  for call in calls:
    if call[0].startswith(f"{caller_prefix}"):
      get_type = get_telephone_type(call[1])
      total += 1
      if get_type == 'Fixed' and call[1].startswith(f"{caller_prefix}"):
          count += 1
  return round(count / total * 100, 2)


print(count_in_state_calls(calls, '(080)'))