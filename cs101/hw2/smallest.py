def smaller(a, b):
    if a < b:
        return a
    else:
        return b

def smallest(a, b, c):
    return smaller(a, smaller(b, c))