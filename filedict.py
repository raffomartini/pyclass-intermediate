''' filedict.py

A dictionary-like object, backed by the filesystem:
- persisten
- concurrent
- shareable with other languages
- introspectable (through the OS)


We will use colleciton.MutableMapping as our guide.
MutableMapping will enforce the dict-like interface.

An ABC is like prefabricated housing.
- you build the foundation (override the abstract methods)
- the ABC then builds the house (mixin methods)
'''

from collections import MutableMapping
import os
import errno

class FileDict(MutableMapping):
    'dict-like, backed by the filesystem'
    # key-value pairs
    # each FileDict stores data in a separate folder
    # key <--> filename
    # value <--> data

    def __init__(self, folder, *args, **kwargs):
        self.folder = folder
        try:
            os.mkdir(folder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                # only escape Error 17 (folder already exsist) exception
                raise # re-raise current exception
        self.update(*args, **kwargs)

    def __repr__(self):
        return '{}({!r}, {!r})'.format(type(self).__name__, self.folder, self.items())

    def __delitem__(self, key):
        filepath = os.path.join(self.folder, key)
        os.remove(filepath)

    def __getitem__(self, key):
        filepath = os.path.join(self.folder, key)
        with open(filepath) as f:
            return f.read()

    def __setitem__(self, key, value):
        filepath = os.path.join(self.folder, key)
        with open(filepath, 'w') as f:
            f.write(repr(value))

    def __len__(self):
        return len(os.listdir(self.folder))
        # os.listdir will return a list of items in the folder

    def __iter__(self):
        # __iter__ is what is called when the iter() method is called on the obj
        return iter(os.listdir(self.folder))


if __name__ == '__main__':
    d = FileDict('starwars')
    d['hero'] = 'Luke'
    d['villain'] = 'Darth Vader'
    print d

    del d['villain']
    d['hero'] = ('Rey', 'Finn')
    print d
    print d.keys()
    print d.values()


