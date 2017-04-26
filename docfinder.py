''' docfinder.py
Keyword-searchable document database.

API:
    create_db() --> None
    add_document(uri, text) --> None
    get_document(uri) --> text of the document
    search(kw0, kw1, kwN) --> URIs of relevant files
    
    Errors: UnknownURI, DuplicateURI
    
    
Tables:
    
    Document
    =============
    uri     text    <-- unique index
    text    blob
    
    Keyword
    ==============
    term    text    <-- index
    score   real
    uri     text
'''

from collections import Counter
from contextlib import closing
import sqlite3, os, bz2, re

__all__ = ['create_db',
           'add_document',
           'get_document',
           'search',
           'UnknownURI',
           'DuplicateURI']

database = 'pepsearch.db'
stopwords = {'and', 'the', 'of', 'it'}

class UnknownURI(Exception):
    'URI not found'

class DuplicateURI(Exception):
    'URI already exist'

def normalize(words):
    '''
    Standardize words into search terms for better comparison
    Lowercase, de-pluralize, ignore stopwords.
    '''
    terms = []

    for word in words:
        #Lowercase,
        lowercased = word.lower()
        # ignore stopwords
        if lowercased not in stopwords:
            # de - pluralize,
            # singular
            singular = lowercased.rstrip('s')
            terms.append(singular)
    return terms

    # lowercased = (word.lower() for word in words)
    # return [word.rstrip('s') for word in lowercased if word not in stopwords]


def score_document(text, n=200, pattern=r'[A-Za-z+]'):
    '''
    Calculate relevance scores for the ``n`` most frequent terms in a document
    '''
    words = re.findall(pattern, text)
    terms = normalize(words)
    counts = Counter(terms).most_common(n)
    total = len(terms)
    return [(term, count/total) for term,count in counts]

def create_db(force=False):
    '''
    Create a new document database.
    if ``force`` delete the old one.
    '''

def add_document(uri, text):
    '''
    Insert a new document in the DB
    '''
def get_document(uri):
    '''
    Fetch a document from the DB
    '''

def search(*keywords):
    '''
    Select URIs of relevant documetns from the DB
    '''