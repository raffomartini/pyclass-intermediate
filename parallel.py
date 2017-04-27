'''


'''

import time, random, itertools
from multiprocessing.pool import ThreadPool
from multiprocessing.pool import Pool
from threading import Lock
# import numpy
# from collections import Counter

def io_bound(x):
    'simulate an i/o-contrained task'
    time.sleep(random.uniform(0,2))
    return x + 1

def cpu_bound(x):
    sum(xrange(int(1e6)))
    # numpy.sum(numpy.arange(1e6, dtype='int'))
    # numpy is quicker because it is compiled in c and is not affected by the multithread lock
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


def multiproc(func, n, maxprocs = 25):
    pool = Pool(min(n, maxprocs))
    for result in pool.imap_unordered(func, range(n)):
        print result


if __name__ == '__main__':
    # start = time.time()
    # serial(cpu_bound, 10)
    # stop = time.time()
    # print 'serial DURATION {:.2f}'.format(stop - start)
    start = time.time()
    threaded(cpu_bound, 10)
    # multiproc(cpu_bound, 10)
    # threaded(cpu_bound, 1000)
    # threaded(tick, 1000)
    stop = time.time()
    print 'parallel DURATION {:.2f}'.format(stop - start)

    # print count