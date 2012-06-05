def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)
    
print factorial(0) # 

# factorial(3)
#   3 * factorial(2)
#     3 * 2 * factorial(1)
#       3 * 2 * 1
#     3 * 2
#   6
# 6