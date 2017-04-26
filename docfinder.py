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
import sql3, os, bz2, re

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

def create_db(force=False):
    '''
    Create a new document database.
    if ``force`` delete the old one.
    '''

def normalize(words):
    '''
    Standardize words into search terms for better comparison
    Lowercase, de-pluralize, ignore stopwords.
    :param words: 
    :return: 
    '''

def score_document(text, n=200, pattern=r'[A-Za-z+]'):
    '''
    Calculate relevance scores for the ``n`` most frequest terms in a document
    :param text: 
    :return: 
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