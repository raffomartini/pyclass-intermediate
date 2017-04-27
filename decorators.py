'''
All about decorators.

Identity Function
    the output is the same as the input
    
Higher-order Function
    receives a functions as input
    add/or returns a function as output
    
Pure Function
    1. always returns the same output for a fiven input
    2. no side-effect (only returns a value)

# Note - printing, writing to a file etc are impure functions

Wrapper Function
    uses another function ("helper")
    typically similar behaviour, but improved
    
Factory Function
    a function that creates and returns a function
    
Closure:
    a place to stash variables from the enclosing scope
    only created for a def in a def
'''

import time, random, math
import functools
# functool has a decorator that helps to change function metadata like names etc
# @functools.wraps() - see below

### Factory functions #########################

def pow2(x):
    return x ** 2

def make_pow(exponent):
    def power(base):
        return base ** exponent
    return power

pow3 = make_pow(3)

pow561 = make_pow(561)

powers = map(make_pow, range(100))

pow8 = make_pow(8)
# print pow8.__closure__[0].cell_contents
# 8

def make_logging(func):
    def logging_wrapper(*args, **kwargs):
        print 'calling', func.__name__
        print 'with', args, kwargs
        result = func(*args, **kwargs)
        print 'result was', result
        return result
    return logging_wrapper

def make_caching(func):
    cache = {}
    def wrapper(*args):
        # to deal with kwargs you'd have to convert them in tuple and sort them
        # kwargs.items().sorted()
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

maxsize = 3
def clearing_cache(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        if len(cache) >= maxsize:
            cache.clear()
        cache[args] = result
        return result
    return wrapper

def random_cache(maxsize=10):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            if args in cache:
                return cache[args]
            result = func(*args)
            if len(cache) >= maxsize:
                del cache[random.choice(list(cache))]
            cache[args] = result
            return result
        return wrapper
    return decorator

# note: original function hidden in the closure
# >>> collatz = make_logging(collatz)
# >>> print collatz.__closure__[0].cell_contents
# <function __main__.collatz>

### Wrapper Functions #########################

def logging_sin(x):
    print 'calling sin'
    print 'with', x
    result = math.sin(x)
    print 'result was', result
    return result

def logging_cos(x):
    print 'calling cos'
    print 'with', x
    result = math.cos(x)
    print 'result was', result
    return result

def better_sqrt(x):
    'sqrt that works on negative inputs'
    if x >= 0:
        return math.sqrt(x)
    return 1j * math.sqrt(-x)

### (Monkey) Patching #########################

import theirs

old_sqrt = math.sqrt

def patch_better_sqrt(x):
    'sqrt that works on negative inputs'
    if x >= 0:
        return old_sqrt(x)
    return 1j * old_sqrt(-x)

math.sqrt = patch_better_sqrt

# print theirs.sqrts([4, 81, -25, 16])


### Higher order functions ####################

def identity(x):
    return x

registry = {}

def register(func):
    registry[func.__name__] = func
    return func

def add_docstring(func):
    if func.__doc__ is None:
        func.__doc__ = 'unknown documentation'
    return func

### Normal functions #########################

def square(x):
    return x ** 2

square = identity(square)
square = register(square)

def power(base, exponent):
    return base ** exponent

power = register(power)
power = add_docstring(power)

# decorating collats, note the order
@make_logging
@register
@add_docstring
def collatz(x):
    'half or triple plus one'
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1

# equivalent
# collatz = register(collatz)
# collatz = add_docstring(collatz)
# collatz = make_logging(collatz)

@make_caching
def conjecture(x):
    'recursing collatz arrives at 1 eventually'
    if x < 1:
        raise ValueError('Must be positive')
    if x == 1:
        return True
    x = collatz(x)
    return conjecture(x)

conjecture = register(conjecture)
conjecture = add_docstring(conjecture)

@random_cache
def hardwork(x):
    print 'doing hard work'
    time.sleep(1)
    return x + 1

cache = {}

def caching_hardwork(x):
    if x in cache:
        return cache[x]
    result = hardwork(x)
    cache[x] = result
    return result

# hardwork = register(hardwork)
# hardwork = add_docstring(hardwork)

# print registry
# help(hardwork)