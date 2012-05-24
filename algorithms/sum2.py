# O(n^2)

s = 0
seq = range(1000)
for x in seq:
    for y in seq:
        s += x*y
print s