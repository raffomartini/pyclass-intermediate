'''
abstract.py

Inheritance is a technique for reusing code across classes.

# Capper and Uncapper are mixins.
Mixins are GREAT!
- Make programming fun an easy
  Writing a new class is just a list of capabilities
  
Mixins are also TERRIBLE :-(
- people accidentally instantiate the mixin
- people forget to implement the required dependencies
 
The solution is Abstract Base Classes (ABCs)

# This is a new style class feature to show the classes it is inheriting from
SkipSeq.__bases__
Out[1]: (__main__.Capper, __main__.Uncapper)

# This is a new style class feature to show the method resolution order
SkipSeq.mro()
Out[2]: [__main__.SkipSeq, __main__.Capper, __main__.Uncapper, object]

# Deck : another tool
- you can append to the deck from both sides
- if the deck has a size, it behaves like a circular buffer
'''


from abc import ABCMeta, abstractmethod
from collections import Sequence
# a Sequence is an iterable, and has a size

class Capper(object):
    'inherit this to gain the uppercasing capability'

    __metaclass__ = ABCMeta

    def capitalize(self):
        return ''.join([c.upper() for c in self])

    @abstractmethod
    def __getitem__(self, index):
        return None

    @abstractmethod
    def __len__(self):
        return 0


class Uncapper(Sequence):
    'inherit this to gain the lowercasing capability'
    #inerithing from Sequence takes away the need of defining __len__ and __getitem__

    def uncapitalize(self):
        return ''.join([c.lower() for c in self])

class SkipSeq(Capper, Uncapper):
    '''
    A sequence that skips very other element.
    
        >>> skip = SkipSeq('abcdefg')
        >>> skip[0]
        'a'
        >>> skip[1]
        'c'
        >>> len(skip)
        4
    '''

    def __init__(self, sequence):
        self.seq = sequence

    def __getitem__(self, index):
        return self.seq[index * 2]

    def __len__(self):
        return (len(self.seq) + 1) // 2

class SkipTwoSeq(Capper, Uncapper):
    '''
    A sequence that keeps every third element.
    
        >>> skip = SkipTwoSeq('abcdefg')
        >>> skip[0]
        'a'
        >>> skip[1]
        'd'
        >>> len(skip)
        3
    '''

    def __init__(self, sequence):
        self.seq = sequence

    def __getitem__(self, index):
        return self.seq[index * 3]

    def __len__(self):
        return (len(self.seq) + 2) // 3

if __name__ == '__main__':
    import doctest
    doctest.testmod()
