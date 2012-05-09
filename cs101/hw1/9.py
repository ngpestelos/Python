# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

#x = 3.14159
#x = 2.5
#x = 2.6
x = 6.349838
s = str(x)

dot = s.find('.')
a = int(s[:dot])

print s[dot+1:][0:1]

b = s[dot+1:][0:1].find('5')
b += s[dot+1:][0:1].find('6')
b += s[dot+1:][0:1].find('7')
b += s[dot+1:][0:1].find('8')
b += s[dot+1:][0:1].find('9')
b += 5

print a + b
