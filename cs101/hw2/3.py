# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
  if a == biggest(a, b, c):
    if b == bigger(b, c):
      return b
    else:
      return c
  if b == biggest(a, b, c):
    if a == bigger(a, c):
      return a
    else:
      return c
  if c == biggest(a, b, c):
    if a == bigger(a, b):
      return a
    else:
      return b

print median(1,2,3)
print median(1,3,2)
print median(3,1,2)
print median(7,8,7)