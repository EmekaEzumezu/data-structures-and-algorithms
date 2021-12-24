"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_dict = {}
for row in calls:
    # Add caller's time making sure there are no duplicate numbers
    if row[0] not in call_dict:
        call_dict[row[0]] = int(row[3])
    else:
        call_dict[row[0]] += int(row[3])
        
    # Add receiver's time making sure there are no duplicate numbers
    if row[1] not in call_dict:
        call_dict[row[1]] = int(row[3])
    else:
        call_dict[row[1]] += int(row[3])

    #call_dict.update({row[0] : row[3]})
    #call_dict.update({row[1] : row[3]})
    
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
max(call_dict, key=call_dict.get), max(call_dict.values())))
#long_time
#print(max(call_dict, key=call_dict.get))
#print(max(call_dict.values()))

