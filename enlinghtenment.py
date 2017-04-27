'''
Medidtate on calsses and closures...

    "Objects are a poor man's closures.
    Closures are a poor man's objects." -- Qc Na
'''

count_a = 0

def tick_a():
    global count_a
    count_a += 1
    return count_a

count_b = 0

def tick_b():
    global count_b
    count_b += 1
    return count_b

### Solution: OOP

class Ticker:

    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1
        return self.count

a = Ticker()
b = Ticker()

### Colution: Closures

def ticker():
    def tick():
        tick.count += 1
        return tick.count
    tick.count = 0
    return tick

tick_a = ticker()
tick_b = ticker()