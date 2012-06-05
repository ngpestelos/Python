# iterative factorial

def factorial(n):
    val = 1
    while n > 1:
        val = n * val
        n = n - 1
    return val

print factorial(2)
print factorial(3)
print factorial(4)
print factorial(5)