def fib(i):
    if i < 2: return 1
    return fib(i - 1) + fib(i - 2)

print fib(10)
print fib(100)