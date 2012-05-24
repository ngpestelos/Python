# O(n^3)

s = 0
seq = range(1000)
for x  in seq:
    for y in seq:
        s += x * y
    for z in seq:
        for w in seq:
            s += x - w
print s