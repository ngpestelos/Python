def proc1(p):
    p[0] = p[1]

def proc2(p):
    p = p + [1]

p = [1,2]
#proc1(p)
proc2(p)
print p