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

def get_all_senders(log, duplicates=False):
    senders = []
    for record in log:
        if duplicates:
            senders.append(record[0])
        else:
            if record[0] not in senders:
                senders.append(record[0])
    return senders

def get_caller_receivers(log, sender, duplicates=False):
    recievers = []
    for record in log:
        if record[0] == sender:
            if duplicates:
                recievers.append(record[1])
            else:
                if record[1] not in recievers:
                    recievers.append(record[1])
    return recievers

def get_number_of_received_actions(log, receiver):
    actions = 0
    for record in log:
        if record[1] == receiver:
            actions += 1
    return actions

def get_number_of_sent_actions(log, sender):
    actions = 0
    for record in log:
        if record[0] == sender:
            actions += 1
    return actions

def get_telemarketers(calls, texts, duplicates=False):
    telemarketers = []
    for sender in get_all_senders(calls):
        actions = get_number_of_received_actions(calls, sender) + get_number_of_received_actions(texts, sender) + get_number_of_sent_actions(texts, sender)
        if actions == 0:
            telemarketers.append(sender)
    return telemarketers

print('These numbers could be telemarketers: \n{}'.format('\n'.join(sorted(get_telemarketers(calls,texts)))))
