# Populate a table with lists of multiples
# (count down)

N = 4

d = {1: [[1]], 2: [[1, 1], [2]], 3: [[1, 1, 1], [3]], 4: [[1, 1, 1, 1], [4], [1, 1, 2], [2, 2]]}

M = 3

for A in d[M]:
    for j in range(M-1, 0, -1):
        for B in d[j]:
            C = A + B
            if (sum(C) > N):
                break
            if (sum(C) == N and C not in d[N]):
                d[N].append(C)

print d