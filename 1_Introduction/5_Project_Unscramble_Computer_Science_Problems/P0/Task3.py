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

# from_banga = 0
# to_banga = 0
# code_list = set()

# for row in calls:
#     if row[0][:5] == "(080)":
        
#         # num of calls fro Bangalore
#         from_banga += 1
        
#         # adding fixed line area codes
#         if row[1][:2] == "(0":
#             # index of the closing bracket ")"
#             ind = row[1].index(")")
            
#             # add to the code list
#             code_list.add(row[1][:ind+1])
            
#         # adding mobile number area codes
#         if row[1][5] == " " and (row[1][0] == "7" or row[1][0] == "8" or row[1][0] == "9"):
#             code_list.add(row[1][:4])
            
#         # adding Telemarketers numbers
#         if row[1][:3] == "140":
#             code_list.add(row[1][:3])
            
#         # num of call to Bangalore
#         if row[1][:5] == "(080)":
#             to_banga += 1
            
# for item in sorted(code_list):            
#     print(item)
    
# # Part B: percentage calls from Bangalore to Bangalore
# per = (to_banga/from_banga) * 100.0
# print("Percentage {:.2f}".format(per))


### REFACTORED

def bangalore_called(call):
    return call[0][:5] == "(080)"

def area_codes(call):
    # adding fixed line area codes
    if call[1][:2] == "(0":
        # index of the closing bracket ")"
        ind = call[1].index(")")

        # add to the code list
        return call[1][:ind+1]

    # adding mobile number area codes
    if call[1][5] == " " and (call[1][0] == "7" or call[1][0] == "8" or call[1][0] == "9"):
        return call[1][:4]

    # adding Telemarketers numbers
    if call[1][:3] == "140":
        return call[1][:3]

            

if __name__ == '__main__':
    
    from_banga = 0
    to_banga = 0
    code_list = set()

    for call in calls:
        if bangalore_called(call):
            
            # Part A: adding area codas
            code_list.add(area_codes(call))
            
            # Part B: % calls in Bangalore
            # num of calls fro Bangalore
            from_banga += 1

            # num of call to Bangalore
            if call[1][:5] == "(080)":
                to_banga += 1

    
# Part A: all of the area codes and mobile prefixes called by people in Bangalore.
print("The numbers called by people in Bangalore have codes:")
#print(code_list)
for item in sorted(code_list):
    print(item)
    
# space between Part A and B
print("\n")
    
# Part B: percentage calls from Bangalore to Bangalore
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    (to_banga/from_banga) * 100.0))
