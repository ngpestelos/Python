# See Data Crunching, p. 23

import sys

count = {}
for address in sys.stdin:
    address = address.rstrip()
    if address not in count:
        count[address] = 1
    else:
        count[address] += 1

addresses = count.keys()
addresses.sort()
for address in addresses:
    print address, count[address]