# 2 GOLD STARS

# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

# Hint: You can not add an integer and a string, but in homework 1.9
# you came across a method, str, for turning an integer into a string.

def print_multiplication_table(n):
  i = 1
  while i <= n:
    j = 1
    while j <= n:
      print str(i), " * ", str(j), " = ", i*j
      j = j + 1
    i = i + 1
    
print_multiplication_table(10)