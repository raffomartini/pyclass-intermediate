"""
Tests for docfinder.py

To use this, grab "data/peps.zip" from the GitHub repository,
then unzip the "peps.zip" archive into the folder "data/peps".
If you are still getting file-not-found errors, please make sure
that the files exist in "data/peps" rather than "data/peps/peps"
"""

from docfinder import *
from docfinder import normalize, score_document
import pprint, os

docdir = 'data/peps'


# Test 1
if 1:
    print list(normalize(['Hettinger', 'enumerates', 'AND']))

# Test 2
if 1:
    filename = 'pep-0238.txt'
    fullname = os.path.join(docdir, filename)
    with open(fullname) as f:
        text = f.read()
    for term, score in score_document(text, n=10):
        print term, score

# Test 3
if 1:
    create_db(force=True)

# Test 4
if 1:
    # for filename in ['pep-0237.txt', 'pep-0236.txt', 'pep-0235.txt']:
    for filename in os.listdir(docdir):
        fullname = os.path.join(docdir, filename)
        with open(fullname, 'rb') as f:
            text = f.read()
        uri = os.path.splitext(filename)[0]
        print uri, len(text)
        add_document(uri, text)
        
# Test 5
if 1:
    print get_document('pep-0237')[:100]
    # print get_document('pep-0383')[:100]

# Test 6
if 1:
    # pprint.pprint(search('zip')[:10])
    pprint.pprint(search('zip', 'barry')[:10])

"""
$ sqlite3 pepsearch.db
SQLite version 3.8.5 2014-08-15 22:37:57
Enter ".help" for usage hints.
sqlite> .tables
Documents  Topics
sqlite> .schema Documents
CREATE TABLE Documents (uri text, document blob);
CREATE UNIQUE INDEX UriIndex ON Documents (uri);
sqlite> .schema Topics
CREATE TABLE Topics (term text, uri text, score real);
CREATE INDEX TermIndex ON Topics (term);
sqlite>
"""
