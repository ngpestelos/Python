from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):                    # Memoize the function
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]              # Return the cached solution
    return wrap                         # Return the wrapped function