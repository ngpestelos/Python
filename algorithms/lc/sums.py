# Generate all linear combinations that add up to a certain positive integer N
# ax1 + bx2 + cx3 + dx4 = N

# Set upper limit and range of coefficients
N = 100
M = range(1, N+1)

# Initialize table
T = {}
for i in M:
    T[i] = []

# Build the lookup table
for i in range(1, N+1):
    for m in M:
        row = i * [m]
        index = sum(row)
        if index > N:
            break
        T[index].append(row)

# Look for optimal LCs on the same column
for j in range(1, N+1):
    for A in T[j]:
        for B in T[j][1:]:
            C = A + B
            C.sort()
            if (sum(C) > N):
                break
            if (sum(C) == N and C not in T[N]):
                T[N].append(C)

# Look down (j-1..1)
for k in range(N-1, 0, -1):
    for A in T[k]:
        for m in range(k-1, 0, -1):
            for B in T[m]:
                C = A + B
                C.sort()
                if (sum(C) > N):
                    break
                if (sum(C) == N and C not in T[N]):
                    T[N].append(C)

print T[N]