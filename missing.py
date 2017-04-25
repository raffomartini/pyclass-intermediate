'''

'''

#old style
class Foo:
    pass

#new style
class Bar(object):
    pass

class AngryDict(dict):
    def __missing__(self, key):
        print 'I am so angry {!r} is missing'.format(key)
        raise KeyError(key)

class ZeroDict(dict):
    def __missing__(self, key):
        return 0

class ListDict(dict):
    def __missing__(self, key):
        value = []
        self[key] = value
        return value

class DefaultFormatDict(dict):
    def __missing__(self, key):
        return '%(' +key + ')s'

class DefaultDict(dict):
    'rough sketch of collection.defaultdict'

    def __init__(self, factory, *args, **kwargs):
        dict.__init__(self,*args,**kwargs)
        self.factory = factory


    def __missing__(self, key):
        value = self.factory()
        self[key] = value
        return value

class ChainDict(dict):
    '''dict that allows cascading lookup to a fallback if keys are missing
    defaults = {'bg': 'black','fg': 'green','h': 24,'w': 40}
    settings = ChainDict(defaults, {'fg': 'cyan', 'h': 40, 'w': 80})
    settings = {'bg': 'black','fg': 'cyan','h': 40, 'w': 80}
    '''
    # collections.ChainMap (available in Python3)

    # locals --> globals --> builtins --> NameError
    # instance --> class --> bases .. --> AttributeError
    # CWD --> $PYTHONPATH --> site-packages --> ImportError
    # $PATH --> 'executable no found"
    # L1 --> l2 --> L3 --> RAM --> virtual memory --> kernel panic!

    def __init__(self, fallback, *args, **kwargs):
        self.fallback = fallback
        self.update(*args, **kwargs)

    def __missing__(self,key):
        return self.fallback[key]

defaults = {'bg': 'black','fg': 'green','h': 24,'w': 40}
settings = ChainDict(defaults, {'fg': 'cyan', 'h': 40, 'w': 80})


# use the missing magic methods to simplify formatting

#step 1
'The answer was %s yesterday, but is %s today' % (5, 10)
# note the % operator is the __mod__ magic method

# Note it works ONLY with tuples:
'The answer was %s yesterday' % [5, 10]
# Out[12]: 'The answer was [5, 10] yesterday'

# How to represent a tuple?
t = (5,10)
'The answer was %s yesterday' % (t,)
# Out[13]: 'The answer was (5, 10) yesterday'


'The answer was {old} yesterday, but is {new} today'.format(**dict(old=5,new=10))

