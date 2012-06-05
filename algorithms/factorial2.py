# print intermediate results

def allFactorials(n):
    results = {}
    doAllFactorials(n, results, 0)
    return results

def doAllFactorials(n, results, level):
    if n > 1:
        results[level] = n * doAllFactorials(n - 1, results, level + 1)
        return results[level]
    else:
        results[level] = 1
        return 1

print allFactorials(3)