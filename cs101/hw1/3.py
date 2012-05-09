x = 0
a = 1

# OK
#a = x
#a = a + 1
#print x, a

# NOT OK
#x = x + 1
#x = x
#print x

# OK
#z = x
#a = z
#x = a
#print x

# OK
#a = x
#x = a
#print x, a

# OK
a, x = x, a
a, x = a, a
print x, a
