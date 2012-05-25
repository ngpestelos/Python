# Simple adjacency set (a set of neighbors for each node in the graph)

a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},    # a 
    {c, e},             # b
    {d},                # c
    {e},                # d
    {f},                # e
    {g, h},             # f
    {f, h},             # g
    {f, g}              # h
]

print N[0]