'''
The famous Fibonacci sequence: 0, 1, 1, 2, 3, 5,...

# counting the calls to line 14
N   recursive   iterative
==  =========   =============
5   19          15
10  276         55         
15  3177        120
20  35400       210
25  392809      325
30  4356586     465
    _ phi ^ N   ~ n ^ phi
'''


def nth(n):
    '''
    The n-th term in the Fibonacci sequence.

        0-th: 0
        1-th: 1
        n-th: (n-1)th + (n-2)th
    '''

    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth(n-1) + nth(n-2)

def nth(n):
    '''
    all recursions can be rewritten as iterations'
    '''
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    import sys
    print sys.argv
    try:
        n = int(sys.argv[1])
    except (IndexError, ValueError):
        n = 10
    for i in range(n):
        print '{}-th:'.format(i), nth(i)