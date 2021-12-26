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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

send_call = set(call[0] for call in calls)
receive_call = set(call[1] for call in calls)
send_text = set(text[0] for text in texts)
receive_text = set(text[1] for text in texts)

if __name__ == '__main__':

    tele_mkt = set()
    for call in send_call:
        if call not in receive_call and call not in send_text and call not in receive_text:
            tele_mkt.add(call)
    print("These numbers could be telemarketers: ")
    for mk in sorted(tele_mkt):
        print(mk)
