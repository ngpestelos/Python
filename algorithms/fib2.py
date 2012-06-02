# Fibonacci, with memoization
from memo import memo

@memo
def fib(i):
    if i < 2: return 1
    return fib(i - 1) + fib(i - 2)

#fib = memo(fib)
print fib(100)