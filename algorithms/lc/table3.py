# Populate a table with lists of multiples
# (completing up to M=4)
# (also counting up)

N = 4   # upper limit
M = 1   # target number
T = {}  # table

for i in range(1, N+1):
    T[i] = []

for i in range(1, N+1):
    T[i].append(i * [M])
    
#print T

M = 2

for i in range(1, N+1):
    row = i * [M]
    index = sum(row)
    if index > N:
        break
    T[index].append(row)

#print T

M = 3

for i in range(1, N+1):
    row = i * [M]
    index = sum(row)
    if index > N:
        break
    T[index].append(row)

#print T

M = 4

for i in range(1, N+1):
    row = i * [M]
    index = sum(row)
    if index > N:
        break
    T[index].append(row)

print T