# Populate a table with lists of multiples
# (count in place)

N = 4

d = {1: [[1]], 2: [[1, 1], [2]], 3: [[1, 1, 1], [3]], 4: [[1, 1, 1, 1], [2, 2], [4]]}

M = 2 # skip 3 for now

for A in d[M]:
    for B in d[M][1:]:
        C = A + B
        if (sum(C) > N):
            break
        if (sum(C) == N and C not in d[N]):
            d[N].append(C)

print d