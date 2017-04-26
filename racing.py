'''
Tracing down race conditions in multithreaded code.
(The easy wasy is using multiprocessing.pool.ThreadPool)

Race conditions:
1- the consumer races ahead of the producer and early-exit before the producer is finished.
    Fix: delay the consumer

2- the main thread can race ahead of the sub-thread and print results before the sub-threads are finished
    Fix: wait until producer and consumer both are finished 
    
3- the consumer threads can race against each others and LBYL pop an empty queue.
    Fix: use EAFP to ensure getting a word is an atomic action
'''

from collections import Counter
import re

counts = Counter()
with open('data/dialogue.txt') as f:
    for line in f:
        for word in re.findall(r'[a-z]+', line.lower()):
            counts[word] +=1

print 'SERIAL VERSION'
print counts.most_common(3)

###########################################
# Threaded version

from collections import Counter
from threading import Thread, Lock
from Queue import Queue
import re

q = Queue()
counts = Counter()
counts_lock = Lock()

def producer(filename):
    'producer thread'
    with open(filename) as f:
        for line in f:
            for word in re.findall(r'[a-z]+', line.lower()):
                q.put(word)

def consumer():
    'consumer thread'
    while True:
        word = q.get()
        with counts_lock:
            counts[word] += 1
        q.task_done()

def main():
    filenames = ['data/dialogue.txt']

    producers = []
    for filename in filenames:
        # producer(filenames[0])
        t = Thread(target=producer, args=(filename,))
        t.start()
        producers.append(t)

    consumers = []
    for i in range(10):
        # producer(filenames[0])
        t = Thread(target=consumer)
        # daemon thread: the program terminates when no alive non daemon threads are left
        t.daemon = True
        t.start()
        consumers.append(t)

    for t in producers:
        t.join()
        # when the thread is over, move on
    q.join()
    # when the queue is empty move on

    print 'PARALLEL VERSION'
    print counts.most_common(3)

if __name__ == '__main__':
    main()