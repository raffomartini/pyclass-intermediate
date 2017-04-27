'''
Keyword-searchable document database.

API:
    create_db(force=False) --> None
    add_document(uri, text) --> None
    get_document(uri) --> text of the document
    search(keyword0, keyword1, ... keywordN) --> URIs of relevant files

    Errors: UnknownURI, DuplicateURI


Tables:

    Document
    ============
    uri     text  <-- unique index
    content blob

    Keyword
    ============
    term    text  <-- index
    score   real
    uri     text
'''

from __future__ import division
from collections import Counter
from contextlib import closing
import sqlite3, os, bz2, re

__all__ = ['create_db',
           'add_document',
           'get_document',
           'search',
           'UnknownURI',
           'DuplicateURI']

# class Database:
#
#     def __init__(self,database):
#         self.database = database

database = 'pepsearch.db'
stopwords = {'and', 'the', 'of', 'it'}

class UnknownURI(Exception):
    'URI not found'

class DuplicateURI(Exception):
    'URI already exists'

def normalize(words):
    '''
    Standardize words into search terms for better comparison.
    Lowecase, de-pluralize, and ignore stopwords.
    '''
    terms = []
    for word in words:
        lowercased = word.lower()
        if lowercased not in stopwords:
            singular = lowercased.rstrip('s')
            terms.append(singular)
    return terms

    # lowercased = (word.lower() for word in words)
    # return [word.rstrip('s') for word in lowercased if word not in stopwords]

def score_document(text, n=200, pattern=r'[A-Za-z]+'):
    '''
    Calculate relevance scores for the ``n`` most
    frequent terms in a document.
    '''
    words = re.findall(pattern, text)
    terms = normalize(words)
    counts = Counter(terms).most_common(n)
    total = len(terms)
    return [(term, count / total) for term, count in counts]

def create_db(force=False):
    '''
    Create a new document database.
    If ``force`` delete the old one.
    '''
    # closing is a context manager form  contextlib,
    # closes everything that implements the method .close()
    if force:
        try:
            os.remove(database)
        except OSError:
            pass # suppress, file not found
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        c.execute('CREATE TABLE Document (uri text, content blob)')
        c.execute('CREATE TABLE Keyword (term text, score real, uri text)')
        c.execute('CREATE UNIQUE INDEX UriIndex ON Document (uri)')
        c.execute('CREATE INDEX TermIndex ON Keyword (term)')

def add_document(uri, text):
    '''
    Insert a new document into the database.
    '''
    blob = sqlite3.Binary(bz2.compress(text))
    # the sqlite3.Binary is helping the parser to sanitize the input in note1
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        try:
            # Note1: used here
            c.execute('INSERT INTO Document VALUES (?, ?)', (uri, blob))
        except sqlite3.IntegrityError:
            raise DuplicateURI(uri)

        args = ((term, score, uri) for term, score in score_document(text))
        c.executemany('INSERT INTO Keyword VALUES (?, ?, ?)', args)

        # for term, score in score_document(text):
        #     c.execute('INSERT INTO Keyword VALUES (?, ?, ?)', (term, score, uri))
        connection.commit()

def get_document(uri):
    '''
    Fetch the content of a document from the database.
    '''
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        c.execute('SELECT content FROM Document WHERE uri = ?', (uri,))
        row = c.fetchone()
        if row is None:
            raise UnknownURI(uri)
        return bz2.decompress(row[0])

def search(*keywords):
    '''
    Select URIs of relevant documents from the database.
    '''

    query_template = '''
    SELECT uri 
    FROM Keyword 
    WHERE term IN ({marks}) 
    GROUP BY uri
    ORDER BY sum(score) DESC
    '''
    terms = normalize(keywords)
    marks = ','.join('?' * len(terms))
    query = query_template.format(marks=marks)
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        c.execute(query, terms)
        rows = c.fetchall()
        return [uri for (uri,) in rows]