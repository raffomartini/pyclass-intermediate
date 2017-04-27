'''


'''

import time, random, itertools
from multiprocessing.pool import ThreadPool
from threading import Lock
# from collections import Counter

def io_bound(x):
    'simulate an i/o-contrained task'
    time.sleep(random.uniform(0,2))
    return x + 1

def cpu_bound(x):
    sum(xrange(int(1e8)))
    return x + 1

count = 0

def racing(x):
    global count
    count += 1
    return x

def tick(x, lock=Lock()):
    global count
    with lock:
        count += 1
    return x

def serial(func, n):
    for result in itertools.imap(func, range(n)):
        print result

def threaded(func, n, maxthread = 25):
    pool = ThreadPool(min(n, maxthread))
    # for result in pool.imap(func, range(n)):
    # imap keeps the thread in order
    # imap_unordered doesn't
    for result in pool.imap_unordered(func, range(n)):
        print result


if __name__ == '__main__':
    start = time.time()
    # serial(cpu_bound, 10)
    threaded(cpu_bound, 10)
    # threaded(cpu_bound, 1000)
    # threaded(tick, 1000)
    stop = time.time()
    print 'DURATION {:.2f}'.format(stop - start)

    # print count