# Populate a table with lists of multiples

N = 4   # upper limit
M = 1   # target number
T = {}  # table

for i in range(1, N+1):
    T[i] = []

for i in range(1, N+1):
    T[i].append(i * [M])
    
print T

M = 2

for i in range(1, N+1):
    row = i * [M]
    index = sum(row)
    if index > N:
        break
    T[index].append(row)

print T

# TODO Count up, then Count down