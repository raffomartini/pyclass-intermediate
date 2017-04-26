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

class FileDict:
    'dict-like, backed by the filesystem'

