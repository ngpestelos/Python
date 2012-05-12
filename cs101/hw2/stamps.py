# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The answer should use as many 5p stamps as possible,
# then 2 pence stamps and finally 1p stamps.

def stamps(n):
  fives = 0
  twos = 0
  ones = 0
  # keep subtracting five
  while n >= 5:
    n = n - 5
    fives = fives + 1
  # keep subtracting two
  while n >= 2:
    n = n - 2
    twos = twos + 1
  # keep subtracting one
  while n >= 1:
    n = n - 1
    ones = ones + 1
  return (fives, twos, ones)


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and one 1p stamp
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps