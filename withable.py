'''
"Context manager are the greatest invention since the subroutine" -- Raymond Hettinger

==========  ====================        ==========================
Op/Fn/Kwd   Magic Methods               Jargon
==========  ====================        ==========================
s + t       s.__add__(t)                Addable
s / t       s.__div__(t)                Divisible
 >> t       s.__repr__()                
print s     s.__str___()                
s[t]        s.__getitem__(t)            Indexable, Subscriptable
for t in s  s.__iter__(t)               Iterable
next(s)     s.next()                    Iterator
s()         s.__call__()                Callable
len(s)      s.__len__()                 Sizeable
with s:     s.__enter() s.__exit__()    Context Manager
==========  ====================        ==========================
'''

# a context manager allows to wrap the try/except/finally in a different form
# These are called python Data Models

import os,sys

def one():
    return 1

def two():
    return 2

registry = {
    int: one,
    str: two
}

class Foo:
    def __add__(self,other):
        try:
            func = registry[type(other)]
        except KeyError:
            raise TypeError('Expected int or str')
    return func()

class ContextManager(object):
    ' a generic context manager'

    def __init__(self,value):
        self.value = value

    def __enter__(self):
        print 'entering the context'

    def __exit__(self, etype, einstance, etraceback):
        print 'leaving the context'
        if isinstance(einstance, RuntimeError):
            print 'marking exception as handled'
            return True

class Suppress(object):
    'suppress errors'
    def __init__(self, etypes):
        self.etypes = etypes

    def __enter__(self):
        return self

    def __exit__(self, etypes, einstances, etraceback):
        if isinstance(einstances, self.etypes):
            return True

# with Suppress(OSError):
#     os.remove('tmp.txt')

class Closing(object):
    'turns any object into a closing context manager'
    # For example can be used to automatically close sockets / files / pipes

    def __init__(self, closeable):
        self.obj = closeable

    def __enter__(self):
        return self.obj

    def __exit__(self, *args):
        self.obj.close()

class RedirectStdout(object):
    'termprarily replace stdout with a different file-like object'

    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.target
        return self

    def __exit__(self, *args):
        sys.stdout = self.old_stdout

'''
Can be used to redirect to stderr
with RedirectStdout(sys.stderr):
    print 'red'
print 'blue'
'''

'''
Can be used to redirect to a file:

with open('topics.txt', 'w') as f:
    with RedirectStdout(f):
        help('topics')

The above will call help('topics') and redirect to the topics.txt file
'''

if __name__ == '__main__':
    with ContextManager(42) as x:
        print 'inside the context'
        print x
        raise RuntimeError('ooops')
        print 'last line in the context'